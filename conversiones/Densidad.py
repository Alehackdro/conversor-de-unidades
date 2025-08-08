def convertir_densidad(unidad_inicial, unidad_final, cantidad): 
    # 1. Mapeo de números a nombres
    unidades = {
        "1": "kg_m3",
        "2": "g_cm3",
        "3": "g_l",
        "4": "lb_ft3", 
        "5": "lb_in3"
    }
    
    # 2. Factores hacia kg/m³ (unidad base)
    factores_por_kg_m3 = {
        "kg_m3": 1.0,
        "g_cm3": 1000.0,
        "g_l": 1.0,
        "lb_ft3": 16.0185,
        "lb_in3": 27679.9
    }
    
    # 3. Convertir números a nombres de unidad si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]
    
    # 4. Validaciones
    if unidad_inicial not in factores_por_kg_m3:
        raise ValueError(f"Unidad inicial '{unidad_inicial}' no válida.")
    if unidad_final not in factores_por_kg_m3:
        raise ValueError(f"Unidad final '{unidad_final}' no válida.")
    
    # 5. Si las unidades son iguales, devolver la cantidad sin cambio
    if unidad_inicial == unidad_final:
        return cantidad
    
    # 6. Cálculo con conversión dinámica
    factor_origen = factores_por_kg_m3[unidad_inicial]
    factor_destino = factores_por_kg_m3[unidad_final]
    factor_conversion = factor_destino / factor_origen
    
    return cantidad * factor_conversion