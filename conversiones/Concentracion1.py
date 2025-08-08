def necesita_parametros_adicionales(unidad_inicial, unidad_final):
    """
    Determina si una conversión de concentración necesita parámetros adicionales.
    
    Args:
        unidad_inicial: Número de unidad inicial (1-12) o nombre de unidad
        unidad_final: Número de unidad final (1-12) o nombre de unidad
    
    Returns:
        dict: Diccionario indicando qué parámetros se necesitan
    """
    
    # Mapeo de números a nombres
    unidades = {
        "1": "molaridad",
        "2": "molalidad", 
        "3": "fraccion_molar",
        "4": "fraccion_masa",
        "5": "milimolar",
        "6": "micromolar",
        "7": "ppm",
        "8": "ppb",
        "9": "g_l",
        "10": "kg_m3",
        "11": "porcentaje_mv",
        "12": "porcentaje_mm"
    }
    
    # Convertir números a nombres si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]
    
    # Unidades que requieren masa molar
    requieren_masa_molar = ["molaridad", "molalidad", "fraccion_molar", "milimolar", "micromolar"]
    
    # Unidades que requieren densidad
    requieren_densidad = ["molalidad", "porcentaje_mm"]
    
    # Conversiones entre fracción masa y fracción molar requieren datos de mezcla
    requiere_datos_mezcla = (
        (unidad_inicial == "fraccion_masa" and unidad_final == "fraccion_molar") or
        (unidad_inicial == "fraccion_molar" and unidad_final == "fraccion_masa")
    )
    
    necesita_masa_molar = (unidad_inicial in requieren_masa_molar or 
                          unidad_final in requieren_masa_molar)
    necesita_densidad = (unidad_inicial in requieren_densidad or 
                        unidad_final in requieren_densidad)
    
    return {
        "masa_molar": necesita_masa_molar and not requiere_datos_mezcla,
        "densidad": necesita_densidad,
        "datos_mezcla": requiere_datos_mezcla
    }

def obtener_datos_mezcla():
    """
    Solicita al usuario los datos de todos los componentes de la mezcla.
    
    Returns:
        list: Lista de diccionarios con 'nombre' y 'peso_molecular' de cada componente
    """
    print("\n" + "="*50)
    print("DATOS DE LA MEZCLA")
    print("="*50)
    print("Para convertir entre fracción masa y fracción molar necesitamos")
    print("información de TODOS los componentes de la mezcla.")
    
    while True:
        try:
            num_componentes = int(input("\n¿Cuántos componentes tiene la mezcla? "))
            if num_componentes < 2:
                print("❌ Una mezcla debe tener al menos 2 componentes.")
                continue
            break
        except ValueError:
            print("❌ Por favor ingrese un número entero válido.")
    
    componentes = []
    
    for i in range(num_componentes):
        print(f"\n--- Componente {i+1} ---")
        nombre = input(f"Nombre del componente {i+1}: ").strip()
        
        while True:
            try:
                peso_molecular = float(input(f"Peso molecular de {nombre} (g/mol): "))
                if peso_molecular <= 0:
                    print("❌ El peso molecular debe ser positivo.")
                    continue
                break
            except ValueError:
                print("❌ Por favor ingrese un número válido.")
        
        componentes.append({
            'nombre': nombre,
            'peso_molecular': peso_molecular
        })
    
    print(f"\n✓ Se registraron {len(componentes)} componentes:")
    for i, comp in enumerate(componentes, 1):
        print(f"  {i}. {comp['nombre']}: {comp['peso_molecular']} g/mol")
    
    return componentes

def convertir_fraccion_masa_a_molar(fraccion_masa, componentes, indice_componente):
    """
    Convierte fracción masa a fracción molar usando la fórmula correcta.
    
    Args:
        fraccion_masa: Fracción masa del componente de interés
        componentes: Lista de componentes con sus pesos moleculares
        indice_componente: Índice del componente de interés (0-based)
    
    Returns:
        float: Fracción molar
    """
    if not (0 <= fraccion_masa <= 1):
        raise ValueError("La fracción masa debe estar entre 0 y 1")
    
    # Calcular el denominador de la fórmula
    denominador = 0
    for i, comp in enumerate(componentes):
        if i == indice_componente:
            # Este es el componente de interés
            denominador += fraccion_masa / comp['peso_molecular']
        else:
            # Para los otros componentes, necesitamos sus fracciones masa
            # Por simplicidad, asumimos distribución uniforme del resto
            fraccion_resto = (1 - fraccion_masa) / (len(componentes) - 1)
            denominador += fraccion_resto / comp['peso_molecular']
    
    # Calcular fracción molar
    numerador = fraccion_masa / componentes[indice_componente]['peso_molecular']
    fraccion_molar = numerador / denominador
    
    return fraccion_molar

def convertir_fraccion_molar_a_masa(fraccion_molar, componentes, indice_componente):
    """
    Convierte fracción molar a fracción masa usando la fórmula correcta.
    
    Args:
        fraccion_molar: Fracción molar del componente de interés
        componentes: Lista de componentes con sus pesos moleculares
        indice_componente: Índice del componente de interés (0-based)
    
    Returns:
        float: Fracción masa
    """
    if not (0 <= fraccion_molar <= 1):
        raise ValueError("La fracción molar debe estar entre 0 y 1")
    
    # Para esta conversión necesitamos las fracciones molares de todos los componentes
    # Por simplicidad, asumimos distribución uniforme del resto
    peso_molecular_promedio = 0
    for i, comp in enumerate(componentes):
        if i == indice_componente:
            peso_molecular_promedio += fraccion_molar * comp['peso_molecular']
        else:
            fraccion_resto = (1 - fraccion_molar) / (len(componentes) - 1)
            peso_molecular_promedio += fraccion_resto * comp['peso_molecular']
    
    # Fracción masa = (fracción molar × peso molecular del componente) / peso molecular promedio
    fraccion_masa = (fraccion_molar * componentes[indice_componente]['peso_molecular']) / peso_molecular_promedio
    
    return fraccion_masa

def convertir_concentracion(unidad_inicial, unidad_final, cantidad, masa_molar=None, densidad=None, datos_mezcla=None):
    """
    Convierte concentraciones entre diferentes unidades.
    
    Args:
        unidad_inicial: Número de unidad inicial (1-12) o nombre de unidad
        unidad_final: Número de unidad final (1-12) o nombre de unidad
        cantidad: Valor de concentración a convertir
        masa_molar: Masa molar del soluto en g/mol (opcional)
        densidad: Densidad de la solución en g/mL (opcional)
        datos_mezcla: Diccionario con datos de mezcla para conversiones fracción masa/molar
    
    Returns:
        float: Concentración convertida
    """
    
    # 1. Mapeo de números a nombres
    unidades = {
        "1": "molaridad",
        "2": "molalidad",
        "3": "fraccion_molar",
        "4": "fraccion_masa",
        "5": "milimolar",
        "6": "micromolar",
        "7": "ppm",
        "8": "ppb",
        "9": "g_l",
        "10": "kg_m3",
        "11": "porcentaje_mv",
        "12": "porcentaje_mm"
    }
    
    # 2. Convertir números a nombres de unidad si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]
    
    # 3. Validaciones
    unidades_validas = list(unidades.values())
    if unidad_inicial not in unidades_validas:
        raise ValueError(f"Unidad inicial '{unidad_inicial}' no válida.")
    if unidad_final not in unidades_validas:
        raise ValueError(f"Unidad final '{unidad_final}' no válida.")
    
    # 4. Si las unidades son iguales, devolver la cantidad sin cambio
    if unidad_inicial == unidad_final:
        return cantidad
    
    # 5. Verificar parámetros necesarios
    parametros = necesita_parametros_adicionales(unidad_inicial, unidad_final)
    
    if parametros["masa_molar"] and masa_molar is None:
        raise ValueError("Esta conversión requiere la masa molar del soluto.")
    if parametros["densidad"] and densidad is None:
        raise ValueError("Esta conversión requiere la densidad de la solución.")
    if parametros["datos_mezcla"] and datos_mezcla is None:
        raise ValueError("Esta conversión requiere datos de la mezcla.")
    
    # 6. Conversión directa entre fracciones masa y molar
    if unidad_inicial == "fraccion_masa" and unidad_final == "fraccion_molar":
        return convertir_fraccion_masa_a_molar(
            cantidad, 
            datos_mezcla['componentes'], 
            datos_mezcla['indice_componente']
        )
    
    if unidad_inicial == "fraccion_molar" and unidad_final == "fraccion_masa":
        return convertir_fraccion_molar_a_masa(
            cantidad, 
            datos_mezcla['componentes'], 
            datos_mezcla['indice_componente']
        )
    
    # 7. Función para convertir a g/L como unidad intermedia
    def a_g_l(valor, unidad, mm=None, dens=None):
        if unidad == "g_l":
            return valor
        elif unidad == "kg_m3":
            return valor  # kg/m³ = g/L
        elif unidad == "ppm":
            return valor / 1000  # ppm a g/L
        elif unidad == "ppb":
            return valor / 1_000_000  # ppb a g/L
        elif unidad == "porcentaje_mv":
            return valor * 10  # %m/v a g/L
        elif unidad == "porcentaje_mm":
            if dens is None:
                raise ValueError("Densidad requerida para % m/m")
            return valor * dens * 10  # %m/m a g/L
        elif unidad == "molaridad":
            if mm is None:
                raise ValueError("Masa molar requerida para molaridad")
            return valor * mm  # M * g/mol = g/L
        elif unidad == "milimolar":
            if mm is None:
                raise ValueError("Masa molar requerida para milimolar")
            return valor * mm / 1000  # mM * g/mol / 1000 = g/L
        elif unidad == "micromolar":
            if mm is None:
                raise ValueError("Masa molar requerida para micromolar")
            return valor * mm / 1_000_000  # μM * g/mol / 1000000 = g/L
        elif unidad == "molalidad":
            if mm is None or dens is None:
                raise ValueError("Masa molar y densidad requeridas para molalidad")
            return valor * mm * dens / (1 + valor * mm / 1000)
        elif unidad in ["fraccion_molar", "fraccion_masa"]:
            raise ValueError(f"Conversión desde {unidad} requiere datos de mezcla específicos")
        else:
            raise ValueError(f"Conversión desde {unidad} no implementada")
    
    # 8. Función para convertir desde g/L
    def desde_g_l(valor, unidad, mm=None, dens=None):
        if unidad == "g_l":
            return valor
        elif unidad == "kg_m3":
            return valor  # g/L = kg/m³
        elif unidad == "ppm":
            return valor * 1000
        elif unidad == "ppb":
            return valor * 1_000_000
        elif unidad == "porcentaje_mv":
            return valor / 10
        elif unidad == "porcentaje_mm":
            if dens is None:
                raise ValueError("Densidad requerida para % m/m")
            return valor / (dens * 10)
        elif unidad == "molaridad":
            if mm is None:
                raise ValueError("Masa molar requerida para molaridad")
            return valor / mm  # g/L / g/mol = M
        elif unidad == "milimolar":
            if mm is None:
                raise ValueError("Masa molar requerida para milimolar")
            return valor * 1000 / mm  # g/L * 1000 / g/mol = mM
        elif unidad == "micromolar":
            if mm is None:
                raise ValueError("Masa molar requerida para micromolar")
            return valor * 1_000_000 / mm  # g/L * 1000000 / g/mol = μM
        elif unidad == "molalidad":
            if mm is None or dens is None:
                raise ValueError("Masa molar y densidad requeridas para molalidad")
            denominador = mm * dens - valor * mm / 1000
            if denominador <= 0:
                raise ValueError("Concentración demasiado alta para conversión a molalidad")
            return valor / denominador * 1000
        elif unidad in ["fraccion_molar", "fraccion_masa"]:
            raise ValueError(f"Conversión hacia {unidad} requiere datos de mezcla específicos")
        else:
            raise ValueError(f"Conversión hacia {unidad} no implementada")
    
    # 9. Realizar la conversión
    try:
        valor_intermedio = a_g_l(cantidad, unidad_inicial, masa_molar, densidad)
        resultado = desde_g_l(valor_intermedio, unidad_final, masa_molar, densidad)
        return resultado
    except Exception as e:
        raise ValueError(f"Error en la conversión: {str(e)}")