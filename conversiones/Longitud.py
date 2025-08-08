def convertir_longitud(unidad_inicial, unidad_final, cantidad):    
    # 1. Mapeo de números a nombres
    unidades = {
        "1": "metros",
        "2": "centimetros",
        "3": "milimetros",
        "4": "kilometros",
        "5": "pulgadas",
        "6": "pies",
        "7": "yardas",
        "8": "millas",
        "9": "micrometros"
    }
    
    # 2. Factores hacia metros (unidad base)
    factores_por_metro = {
        "metros": 1.0,
        "centimetros": 100.0,
        "milimetros": 1000.0,
        "kilometros": 0.001,
        "pulgadas": 39.3701,
        "pies": 3.28084,
        "yardas": 1.09361,
        "millas": 0.000621371,
        "micrometros": 1_000_000.0
    }
    
    # 3. Convertir números a nombres de unidad si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]
    
    # 4. Validaciones
    if unidad_inicial not in factores_por_metro:
        raise ValueError(f"Unidad inicial '{unidad_inicial}' no válida.")
    if unidad_final not in factores_por_metro:
        raise ValueError(f"Unidad final '{unidad_final}' no válida.")
    
    # 5. Si las unidades son iguales, devolver la cantidad sin cambio
    if unidad_inicial == unidad_final:
        return cantidad
    
    # 6. Cálculo con conversión dinámica
    factor_origen = factores_por_metro[unidad_inicial]
    factor_destino = factores_por_metro[unidad_final]
    factor_conversion = factor_destino / factor_origen
    
    return cantidad * factor_conversion