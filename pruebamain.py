# ============================================================================
# PROGRAMA PRINCIPAL - main.py
# ============================================================================

from conversiones.Area import convertir_area
from conversiones.Concentracion import (necesita_parametros_adicionales, convertir_concentracion, obtener_datos_mezcla, calcular_fracciones_mezcla_binaria, convertir_fraccion_masa_a_molar, convertir_fraccion_molar_a_masa)
from conversiones.Temperatura import convertir_temperatura
from conversiones.Densidad import convertir_densidad
from conversiones.Energia import convertir_energia
from conversiones.Longitud import convertir_longitud
from conversiones.Masa import convertir_masa
from conversiones.Presion import convertir_presion
from conversiones.Velocidad import convertir_velocidad
from conversiones.Volumen import convertir_volumen


def mostrar_menu_principal():
    """Muestra el menú principal de tipos de conversión."""
    print("=" * 60)
    print("           CONVERSOR DE UNIDADES")
    print("=" * 60)
    print("Seleccione el tipo de conversión:")
    print("1. Volumen")
    print("2. Temperatura") 
    print("3. Concentración")
    print("4. Densidad")
    print("5. Velocidad")
    print("6. Masa")
    print("7. Energía")
    print("8. Presión")
    print("9. Longitud")
    print("10. Área")
    print("11. Ayuda y ejemplos")
    print("0. Salir")
    print("-" * 60)

def manejar_conversion_generica(tipo_conversion, funcion_convertir, unidades_disponibles, nombres_unidades):
    """
    Maneja conversiones generales para la mayoría de tipos de unidades.
    
    Args:
        tipo_conversion: Nombre del tipo de conversión (ej: "Volumen", "Masa")
        funcion_convertir: Función de conversión específica
        unidades_disponibles: Lista de unidades disponibles
        nombres_unidades: Diccionario con nombres de unidades
    """
    print(f"\nUnidades de {tipo_conversion.lower()} disponibles:")
    for unidad in unidades_disponibles:
        print(unidad)
    
    unidad_inicial = input("Ingrese el número de la unidad inicial: ").strip()
    unidad_final = input("Ingrese el número de la unidad final: ").strip()
    
    try:
        cantidad = float(input("Ingrese la cantidad a convertir: "))
        
        resultado = funcion_convertir(unidad_inicial, unidad_final, cantidad)
        
        nombre_inicial = nombres_unidades.get(unidad_inicial, unidad_inicial)
        nombre_final = nombres_unidades.get(unidad_final, unidad_final)
        
        # Formatear resultado según la magnitud
        if abs(resultado) < 0.001 or abs(resultado) > 1000000:
            print(f"\n✓ Resultado: {cantidad} {nombre_inicial} = {resultado:.2e} {nombre_final}")
        else:
            print(f"\n✓ Resultado: {cantidad} {nombre_inicial} = {resultado:.6f} {nombre_final}")
        
        return resultado
        
    except ValueError as e:
        print(f"❌ Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None

def manejar_conversion_volumen():
    """Maneja la conversión de unidades de volumen."""
    unidades_disponibles = [
        "1. Litros (L)",
        "2. Mililitros (mL)",
        "3. Centímetros cúbicos (cm³)",
        "4. Metros cúbicos (m³)",
        "5. Galones",
        "6. Onzas líquidas (fl oz)",
        "7. Pintas",
        "8. Cuartos",
        "9. Decilitros (dL)",
        "10. Hectolitros (hL)",
        "11. Microlitros (μL)",
        "12. Nanolitros (nL)",
        "13. Barriles",
        "14. Pies cúbicos (ft³)",
        "15. Pulgadas cúbicas (in³)",
        "16. Yardas cúbicas (yd³)"
    ]
    
    nombres_unidades = {
        "1": "Litros", "2": "Mililitros", "3": "Centímetros cúbicos",
        "4": "Metros cúbicos", "5": "Galones", "6": "Onzas líquidas",
        "7": "Pintas", "8": "Cuartos", "9": "Decilitros",
        "10": "Hectolitros", "11": "Microlitros", "12": "Nanolitros",
        "13": "Barriles", "14": "Pies cúbicos", "15": "Pulgadas cúbicas",
        "16": "Yardas cúbicas"
    }
    
    return manejar_conversion_generica("Volumen", convertir_volumen, unidades_disponibles, nombres_unidades)

def manejar_conversion_temperatura():
    """Maneja la conversión de unidades de temperatura."""
    unidades_disponibles = [
        "1. Celsius (°C)",
        "2. Fahrenheit (°F)",
        "3. Kelvin (K)",
        "4. Rankine (°R)",
        "5. Réaumur (°Ré)"
    ]
    
    nombres_unidades = {
        "1": "Celsius", "2": "Fahrenheit", "3": "Kelvin",
        "4": "Rankine", "5": "Réaumur"
    }
    
    return manejar_conversion_generica("Temperatura", convertir_temperatura, unidades_disponibles, nombres_unidades)

def manejar_conversion_densidad():
    """Maneja la conversión de unidades de densidad."""
    unidades_disponibles = [
        "1. kg/m³",
        "2. g/cm³",
        "3. g/L",
        "4. lb/ft³",
        "5. lb/in³"
    ]
    
    nombres_unidades = {
        "1": "kg/m³", "2": "g/cm³", "3": "g/L",
        "4": "lb/ft³", "5": "lb/in³"
    }
    
    return manejar_conversion_generica("Densidad", convertir_densidad, unidades_disponibles, nombres_unidades)

def manejar_conversion_velocidad():
    """Maneja la conversión de unidades de velocidad."""
    unidades_disponibles = [
        "1. m/s (metros por segundo)",
        "2. km/h (kilómetros por hora)",
        "3. mph (millas por hora)",
        "4. ft/s (pies por segundo)",
        "5. nudos (knots)"
    ]
    
    nombres_unidades = {
        "1": "m/s", "2": "km/h", "3": "mph",
        "4": "ft/s", "5": "nudos"
    }
    
    return manejar_conversion_generica("Velocidad", convertir_velocidad, unidades_disponibles, nombres_unidades)

def manejar_conversion_masa():
    """Maneja la conversión de unidades de masa."""
    unidades_disponibles = [
        "1. Kilogramos (kg)",
        "2. Gramos (g)",
        "3. Libras (lb)",
        "4. Miligramos (mg)",
        "5. Toneladas (t)",
        "6. Onzas (oz)",
        "7. Piedras (stone)",
        "8. Toneladas métricas",
        "9. Toneladas cortas"
    ]
    
    nombres_unidades = {
        "1": "Kilogramos", "2": "Gramos", "3": "Libras",
        "4": "Miligramos", "5": "Toneladas", "6": "Onzas",
        "7": "Piedras", "8": "Toneladas métricas", "9": "Toneladas cortas"
    }
    
    return manejar_conversion_generica("Masa", convertir_masa, unidades_disponibles, nombres_unidades)

def manejar_conversion_energia():
    """Maneja la conversión de unidades de energía."""
    unidades_disponibles = [
        "1. Joules (J)",
        "2. Calorías (cal)",
        "3. Kilocalorías (kcal)",
        "4. Electronvoltios (eV)",
        "5. Kilojoules (kJ)",
        "6. BTU",
        "7. Vatios-hora (Wh)",
        "8. Kilovatios-hora (kWh)"
    ]
    
    nombres_unidades = {
        "1": "Joules", "2": "Calorías", "3": "Kilocalorías",
        "4": "Electronvoltios", "5": "Kilojoules", "6": "BTU",
        "7": "Vatios-hora", "8": "Kilovatios-hora"
    }
    
    return manejar_conversion_generica("Energía", convertir_energia, unidades_disponibles, nombres_unidades)

def manejar_conversion_presion():
    """Maneja la conversión de unidades de presión."""
    unidades_disponibles = [
        "1. Pascales (Pa)",
        "2. Kilopascales (kPa)",
        "3. Bar",
        "4. Atmósferas (atm)",
        "5. mmHg (torr)",
        "6. PSI",
        "7. Torr",
        "8. kgf/cm²",
        "9. inHg (pulgadas de mercurio)",
        "10. inH2O (pulgadas de agua)",
        "11. mmH2O (milímetros de agua)"
    ]
    
    nombres_unidades = {
        "1": "Pascales", "2": "Kilopascales", "3": "Bar",
        "4": "Atmósferas", "5": "mmHg", "6": "PSI",
        "7": "Torr", "8": "kgf/cm²", "9": "inHg",
        "10": "inH2O", "11": "mmH2O"
    }
    
    return manejar_conversion_generica("Presión", convertir_presion, unidades_disponibles, nombres_unidades)

def manejar_conversion_longitud():
    """Maneja la conversión de unidades de longitud."""
    unidades_disponibles = [
        "1. Metros (m)",
        "2. Centímetros (cm)",
        "3. Milímetros (mm)",
        "4. Kilómetros (km)",
        "5. Pulgadas (in)",
        "6. Pies (ft)",
        "7. Yardas (yd)",
        "8. Millas",
        "9. Micrómetros (μm)"
    ]
    
    nombres_unidades = {
        "1": "Metros", "2": "Centímetros", "3": "Milímetros",
        "4": "Kilómetros", "5": "Pulgadas", "6": "Pies",
        "7": "Yardas", "8": "Millas", "9": "Micrómetros"
    }
    
    return manejar_conversion_generica("Longitud", convertir_longitud, unidades_disponibles, nombres_unidades)

def manejar_conversion_area():
    """Maneja la conversión de unidades de área."""
    unidades_disponibles = [
        "1. Metros cuadrados (m²)",
        "2. Centímetros cuadrados (cm²)",
        "3. Milímetros cuadrados (mm²)",
        "4. Kilómetros cuadrados (km²)",
        "5. Pulgadas cuadradas (in²)",
        "6. Pies cuadrados (ft²)",
        "7. Yardas cuadradas (yd²)",
        "8. Hectáreas (ha)",
        "9. Acres"
    ]
    
    nombres_unidades = {
        "1": "m²", "2": "cm²", "3": "mm²",
        "4": "km²", "5": "in²", "6": "ft²",
        "7": "yd²", "8": "Hectáreas", "9": "Acres"
    }
    
    return manejar_conversion_generica("Área", convertir_area, unidades_disponibles, nombres_unidades)

def mostrar_resultados_fraccion_binaria(resultado, cantidad, nombres_unidades, unidad_inicial, unidad_final):
    """Muestra los resultados detallados para conversiones de fracciones binarias."""
    print(f"\n✓ RESULTADOS PARA MEZCLA BINARIA:")
    print("=" * 50)
    print(f"📊 Componente de interés: {resultado['componente_interes']}")
    print(f"📊 Otro componente: {resultado['otro_componente']}")
    print("-" * 50)
    
    nombre_inicial = nombres_unidades.get(unidad_inicial, unidad_inicial)
    nombre_final = nombres_unidades.get(unidad_final, unidad_final)
    
    if unidad_inicial == "4":  # fraccion_masa
        valor_convertido = resultado['fraccion_molar_interes']
        print(f"🔄 Conversión solicitada:")
        print(f"   {cantidad} {nombre_inicial} = {valor_convertido:.6f} {nombre_final}")
        print(f"\n📋 Fracciones completas de la mezcla:")
        print(f"   Fracción masa {resultado['componente_interes']}: {resultado['fraccion_masa_interes']:.6f}")
        print(f"   Fracción masa {resultado['otro_componente']}: {resultado['fraccion_masa_otro']:.6f}")
        print(f"   Fracción molar {resultado['componente_interes']}: {resultado['fraccion_molar_interes']:.6f}")
        print(f"   Fracción molar {resultado['otro_componente']}: {resultado['fraccion_molar_otro']:.6f}")
    else:  # fraccion_molar
        valor_convertido = resultado['fraccion_masa_interes']
        print(f"🔄 Conversión solicitada:")
        print(f"   {cantidad} {nombre_inicial} = {valor_convertido:.6f} {nombre_final}")
        print(f"\n📋 Fracciones completas de la mezcla:")
        print(f"   Fracción molar {resultado['componente_interes']}: {resultado['fraccion_molar_interes']:.6f}")
        print(f"   Fracción molar {resultado['otro_componente']}: {resultado['fraccion_molar_otro']:.6f}")
        print(f"   Fracción masa {resultado['componente_interes']}: {resultado['fraccion_masa_interes']:.6f}")
        print(f"   Fracción masa {resultado['otro_componente']}: {resultado['fraccion_masa_otro']:.6f}")
    


def manejar_conversion_concentracion():
    """Maneja la conversión de unidades de concentración."""
    print("\nUnidades de concentración disponibles:")
    print("1. Molaridad (mol/L)")
    print("2. Molalidad (mol/kg)")
    print("3. Fracción molar")
    print("4. Fracción masa")
    print("5. Milimolar (mmol/L)")
    print("6. Micromolar (μmol/L)")
    print("7. ppm (mg/L)")
    print("8. ppb (μg/L)")
    print("9. g/L")
    print("10. kg/m³")
    print("11. % m/v")
    print("12. % m/m")
    
    unidad_inicial = input("Ingrese el número de la unidad inicial: ").strip()
    unidad_final = input("Ingrese el número de la unidad final: ").strip()
    
    try:
        cantidad = float(input("Ingrese la cantidad a convertir: "))
        
        # Verificar si se necesitan parámetros adicionales
        parametros_necesarios = necesita_parametros_adicionales(unidad_inicial, unidad_final)
        
        masa_molar = None
        densidad = None
        datos_mezcla = None
        
        # Manejar conversiones entre fracciones masa y molar
        if parametros_necesarios["datos_mezcla"]:
            print("\n" + "="*60)
            print("⚠️  CONVERSIÓN ENTRE FRACCIÓN MASA Y FRACCIÓN MOLAR")
            print("="*60)
            print("Esta conversión requiere información de TODOS los componentes")
            print("de la mezcla y sus respectivos pesos moleculares.")
            
            componentes = obtener_datos_mezcla()
            
            print(f"\n¿Cuál es el componente de interés para la conversión?")
            for i, comp in enumerate(componentes, 1):
                print(f"{i}. {comp['nombre']}")
            
            while True:
                try:
                    indice_seleccion = int(input("Seleccione el número del componente: ")) - 1
                    if 0 <= indice_seleccion < len(componentes):
                        break
                    else:
                        print(f"❌ Seleccione un número entre 1 y {len(componentes)}")
                except ValueError:
                    print("❌ Por favor ingrese un número válido.")
            
            componente_interes = componentes[indice_seleccion]['nombre']
            print(f"\n✓ Componente seleccionado: {componente_interes}")
            
            datos_mezcla = {
                'componentes': componentes,
                'indice_componente': indice_seleccion
            }
        
        else:
            # Manejar parámetros tradicionales
            if parametros_necesarios["masa_molar"]:
                print("\n⚠️  Esta conversión requiere la masa molar del soluto.")
                print("💡 Ejemplos: NaCl = 58.44 g/mol, Glucosa = 180.16 g/mol")
                masa_molar = float(input("Ingrese la masa molar del soluto (g/mol): ").strip())
            
            if parametros_necesarios["densidad"]:
                print("\n⚠️  Esta conversión requiere la densidad de la solución.")
                print("💡 Para soluciones acuosas diluidas, use ~1.0 g/mL")
                densidad = float(input("Ingrese la densidad de la solución (g/mL): ").strip())
        
        resultado = convertir_concentracion(
            unidad_inicial, unidad_final, cantidad, 
            masa_molar=masa_molar, densidad=densidad, datos_mezcla=datos_mezcla
        )
        
        nombres_unidades = {
            "1": "Molaridad", "2": "Molalidad", "3": "Fracción molar",
            "4": "Fracción masa", "5": "Milimolar", "6": "Micromolar", 
            "7": "ppm", "8": "ppb", "9": "g/L", "10": "kg/m³",
            "11": "% m/v", "12": "% m/m"
        }
        
        # Verificar si el resultado es un diccionario (mezcla binaria) o un float
        if isinstance(resultado, dict) and 'componente_interes' in resultado:
            # Mezcla binaria - mostrar resultados detallados
            mostrar_resultados_fraccion_binaria(resultado, cantidad, nombres_unidades, unidad_inicial, unidad_final)
            
            # Extraer el valor específico convertido para el retorno
            if unidad_inicial == "4":  # fraccion_masa a fraccion_molar
                valor_retorno = resultado['fraccion_molar_interes']
            else:  # fraccion_molar a fraccion_masa
                valor_retorno = resultado['fraccion_masa_interes']
            
        else:
            # Conversión normal - mostrar resultado simple
            nombre_inicial = nombres_unidades.get(unidad_inicial, unidad_inicial)
            nombre_final = nombres_unidades.get(unidad_final, unidad_final)
            valor_retorno = resultado
            
            # Formatear resultado según la magnitud
            if valor_retorno < 0.001:
                print(f"\n✓ Resultado: {cantidad} {nombre_inicial} = {valor_retorno:.2e} {nombre_final}")
            elif valor_retorno > 1000000:
                print(f"\n✓ Resultado: {cantidad} {nombre_inicial} = {valor_retorno:.2e} {nombre_final}")
            else:
                print(f"\n✓ Resultado: {cantidad} {nombre_inicial} = {valor_retorno:.6f} {nombre_final}")
        
        # Mostrar información adicional utilizada
        if masa_molar:
            print(f"📊 Masa molar utilizada: {masa_molar} g/mol")
        if densidad:
            print(f"📊 Densidad utilizada: {densidad} g/mL")
        if datos_mezcla and not isinstance(resultado, dict):
            print(f"📊 Componente de interés: {datos_mezcla['componentes'][datos_mezcla['indice_componente']]['nombre']}")
            print(f"📊 Componentes de la mezcla: {len(datos_mezcla['componentes'])}")
        
        return valor_retorno
        
    except ValueError as e:
        print(f"❌ Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None

def mostrar_ayuda():
    """Muestra ayuda y ejemplos de uso."""
    print("\n" + "=" * 60)
    print("                    AYUDA Y EJEMPLOS")
    print("=" * 60)
    print("📖 CÓMO USAR EL CONVERSOR:")
    print("1. Seleccione el tipo de conversión del menú principal")
    print("2. Elija la unidad inicial escribiendo su número")
    print("3. Elija la unidad final escribiendo su número")
    print("4. Ingrese la cantidad a convertir")
    print("5. ¡Obtenga su resultado!")
    
    print("\n💡 EJEMPLOS RÁPIDOS:")
    print("• Volumen: 1 litro = 1000 mililitros")
    print("• Temperatura: 0°C = 32°F = 273.15K")
    print("• Masa: 1 kg = 2.20462 libras")
    print("• Velocidad: 100 km/h = 27.78 m/s")
    print("• Presión: 1 atm = 101325 Pa")
    print("• Longitud: 1 metro = 100 centímetros = 3.28 pies")
    print("• Área: 1 m² = 10,000 cm² = 10.76 ft²")
    print("• Energía: 1 kWh = 3.6 MJ = 860 kcal")
    print("• Densidad: 1 g/cm³ = 1000 kg/m³")
    
    print("\n🧪 CONCENTRACIONES ESPECIALES:")
    print("• Fracción molar: Proporción de moles de soluto respecto al total")
    print("• Fracción masa: Proporción de masa de soluto respecto al total")
    print("• Para conversiones entre fracción masa/molar se requieren:")
    print("  - Datos de TODOS los componentes de la mezcla")
    print("  - Pesos moleculares de cada componente")
    print("  - Identificar el componente de interés")
    
    print("\n⚠️  NOTAS IMPORTANTES:")
    print("• Para concentraciones, algunas conversiones requieren parámetros adicionales")
    print("• Use punto (.) como separador decimal: 1.5 en lugar de 1,5")
    print("• Los resultados se muestran con alta precisión")
    print("• Las fracciones (molar/masa) deben ser menores que 1")
    print("• Conversiones fracción masa ↔ fracción molar requieren datos completos de mezcla")
    
    print("\n🎯 CONSEJOS:")
    print("• Verifique siempre las unidades antes de confirmar")
    print("• Para valores muy grandes o pequeños, se usa notación científica")
    print("• Para mezclas complejas, tenga listos todos los pesos moleculares")
    print("• Presione Ctrl+C en cualquier momento para salir")

def conversion_unidades():
    """Función principal del conversor de unidades."""
    
    # Mapeo de opciones a funciones
    conversiones = {
        "1": manejar_conversion_volumen,
        "2": manejar_conversion_temperatura,
        "3": manejar_conversion_concentracion,
        "4": manejar_conversion_densidad,
        "5": manejar_conversion_velocidad,
        "6": manejar_conversion_masa,
        "7": manejar_conversion_energia,
        "8": manejar_conversion_presion,
        "9": manejar_conversion_longitud,
        "10": manejar_conversion_area,
        "11": mostrar_ayuda
    }
    
    print("🔧 Bienvenido al Conversor de Unidades Científicas")
    print("📋 Versión completa - Todas las conversiones implementadas")
    
    while True:
        try:
            mostrar_menu_principal()
            opcion = input("Seleccione una opción (0-11): ").strip()
            
            if opcion == "0":
                print("\n🎉 ¡Gracias por usar el conversor de unidades!")
                print("Desarrollado para facilitar tus cálculos científicos 👋")
                break
            
            if opcion in conversiones:
                print("-" * 60)
                resultado = conversiones[opcion]()
                
                if opcion == "11":  # Ayuda no devuelve resultado
                    continue
                
                if resultado is not None:
                    # Preguntar si quiere hacer otra conversión
                    print("\n" + "=" * 30)
                    continuar = input("¿Desea realizar otra conversión? (s/n): ").lower().strip()
                    if continuar not in ['s', 'si', 'sí', 'y', 'yes']:
                        print("\n🎉 ¡Gracias por usar el conversor de unidades! 👋")
                        break
                else:
                    print("\n🔄 Intente nuevamente con valores válidos...")
                    
            else:
                print("❌ Opción no válida. Por favor, seleccione un número del 0 al 11.")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            print("🔄 Intente nuevamente...")

# Ejecutar el programa
if __name__ == "__main__":
    conversion_unidades()