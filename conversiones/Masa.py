def convertir_masa(unidad_inicial, unidad_final, cantidad):
    # 1. Mapeo de números a nombres
    unidades = {
        "1": "kg",
        "2": "g",
        "3": "lb",
        "4": "mg",
        "5": "t",
        "6": "oz",
        "7": "stone",
        "8": "toneladas_metricas",
        "9": "toneladas_cortas"
    }
    
    # 2. Factores hacia kilogramos (unidad base)
    factores_por_kg = {
        "kg": 1.0,
        "g": 1000.0,
        "lb": 2.20462,
        "mg": 1_000_000.0,
        "t": 0.001,
        "oz": 35.274,
        "stone": 0.157473,
        "toneladas_metricas": 0.001,
        "toneladas_cortas": 0.00110231
    }
    
    # 3. Convertir números a nombres de unidad si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]
    
    # 4. Validaciones
    if unidad_inicial not in factores_por_kg:
        raise ValueError(f"Unidad inicial '{unidad_inicial}' no válida.")
    if unidad_final not in factores_por_kg:
        raise ValueError(f"Unidad final '{unidad_final}' no válida.")
    
    # 5. Si las unidades son iguales, devolver la cantidad sin cambio
    if unidad_inicial == unidad_final:
        return cantidad
    
    # 6. Cálculo con conversión dinámica
    factor_origen = factores_por_kg[unidad_inicial]
    factor_destino = factores_por_kg[unidad_final]
    factor_conversion = factor_destino / factor_origen
    
    return cantidad * factor_conversion