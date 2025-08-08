# conversiones.py - Módulo de conversiones de concentración mejorado

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

def calcular_fracciones_mezcla_binaria(fraccion_componente_1, peso_mol_1, peso_mol_2, tipo_inicial):
    """
    Calcula todas las fracciones (masa y molar) para una mezcla binaria.
    
    Args:
        fraccion_componente_1: Fracción del componente 1 (masa o molar según tipo_inicial)
        peso_mol_1: Peso molecular del componente 1
        peso_mol_2: Peso molecular del componente 2
        tipo_inicial: "masa" o "molar" - tipo de la fracción inicial
    
    Returns:
        dict: Diccionario con todas las fracciones calculadas
    """
    
    if not (0 <= fraccion_componente_1 <= 1):
        raise ValueError(f"La fracción {tipo_inicial} debe estar entre 0 y 1")
    
    if tipo_inicial == "masa":
        # Tenemos fracción masa del componente 1
        w1 = fraccion_componente_1
        w2 = 1 - w1
        
        # Calcular fracciones molares
        # n1 = w1/M1, n2 = w2/M2
        # x1 = n1/(n1+n2) = (w1/M1)/((w1/M1) + (w2/M2))
        denominador = (w1/peso_mol_1) + (w2/peso_mol_2)
        x1 = (w1/peso_mol_1) / denominador
        x2 = 1 - x1
        
        return {
            'fraccion_masa_1': w1,
            'fraccion_masa_2': w2,
            'fraccion_molar_1': x1,
            'fraccion_molar_2': x2
        }
    
    elif tipo_inicial == "molar":
        # Tenemos fracción molar del componente 1
        x1 = fraccion_componente_1
        x2 = 1 - x1
        
        # Calcular fracciones masa
        # Peso molecular promedio de la mezcla
        peso_mol_promedio = x1 * peso_mol_1 + x2 * peso_mol_2
        
        # w1 = (x1 * M1) / peso_mol_promedio
        w1 = (x1 * peso_mol_1) / peso_mol_promedio
        w2 = 1 - w1
        
        return {
            'fraccion_masa_1': w1,
            'fraccion_masa_2': w2,
            'fraccion_molar_1': x1,
            'fraccion_molar_2': x2
        }
    
    else:
        raise ValueError("tipo_inicial debe ser 'masa' o 'molar'")

def convertir_fraccion_masa_a_molar(fraccion_masa, componentes, indice_componente):
    """
    Convierte fracción masa a fracción molar usando el método original para multi-componente.
    
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
    Convierte fracción molar a fracción masa usando el método original para multi-componente.
    
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
        dict o float: Para fracciones binarias devuelve dict con todas las fracciones, sino float
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
    
    # 6. Conversión especial entre fracciones masa y molar
    if ((unidad_inicial == "fraccion_masa" and unidad_final == "fraccion_molar") or
        (unidad_inicial == "fraccion_molar" and unidad_final == "fraccion_masa")):
        
        componentes = datos_mezcla['componentes']
        indice_componente = datos_mezcla['indice_componente']
        
        if len(componentes) == 2:
            # Mezcla binaria - calcular todas las fracciones
            if indice_componente == 0:
                peso_mol_1 = componentes[0]['peso_molecular']
                peso_mol_2 = componentes[1]['peso_molecular']
                fraccion_comp_1 = cantidad
            else:
                peso_mol_1 = componentes[1]['peso_molecular'] 
                peso_mol_2 = componentes[0]['peso_molecular']
                fraccion_comp_1 = cantidad
            
            tipo_inicial = "masa" if unidad_inicial == "fraccion_masa" else "molar"
            
            resultados = calcular_fracciones_mezcla_binaria(
                fraccion_comp_1, peso_mol_1, peso_mol_2, tipo_inicial
            )
            
            # Reorganizar resultados según el orden original de componentes
            if indice_componente == 0:
                return {
                    'componente_interes': componentes[0]['nombre'],
                    'otro_componente': componentes[1]['nombre'],
                    'fraccion_masa_interes': resultados['fraccion_masa_1'],
                    'fraccion_masa_otro': resultados['fraccion_masa_2'],
                    'fraccion_molar_interes': resultados['fraccion_molar_1'],
                    'fraccion_molar_otro': resultados['fraccion_molar_2']
                }
            else:
                return {
                    'componente_interes': componentes[1]['nombre'],
                    'otro_componente': componentes[0]['nombre'],
                    'fraccion_masa_interes': resultados['fraccion_masa_1'],
                    'fraccion_masa_otro': resultados['fraccion_masa_2'],
                    'fraccion_molar_interes': resultados['fraccion_molar_1'],
                    'fraccion_molar_otro': resultados['fraccion_molar_2']
                }
        else:
            # Mezcla con más de 2 componentes - usar método original
            if unidad_inicial == "fraccion_masa":
                resultado = convertir_fraccion_masa_a_molar(
                    cantidad, componentes, indice_componente
                )
            else:
                resultado = convertir_fraccion_molar_a_masa(
                    cantidad, componentes, indice_componente
                )
            return resultado
    
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
    
    # 9. Realizar la conversión normal
    try:
        valor_intermedio = a_g_l(cantidad, unidad_inicial, masa_molar, densidad)
        resultado = desde_g_l(valor_intermedio, unidad_final, masa_molar, densidad)
        return resultado
    except Exception as e:
        raise ValueError(f"Error en la conversión: {str(e)}")