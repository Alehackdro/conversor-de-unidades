def convertir_area(unidad_inicial, unidad_final, cantidad):
    # 1. Mapeo de números a nombres
    unidades = {
        "1": "metros_cuadrados",
        "2": "centimetros_cuadrados",
        "3": "milimetros_cuadrados",
        "4": "kilometros_cuadrados",
        "5": "pulgadas_cuadradas",
        "6": "pies_cuadrados",
        "7": "yardas_cuadradas",
        "8": "hectareas",
        "9": "acres"
    }
    
    # 2. Factores hacia metros cuadrados (unidad base)
    factores_por_m2 = {
        "metros_cuadrados": 1.0,
        "centimetros_cuadrados": 10000.0,
        "milimetros_cuadrados": 1_000_000.0,
        "kilometros_cuadrados": 0.000001,
        "pulgadas_cuadradas": 1550.0031,
        "pies_cuadrados": 10.7639,
        "yardas_cuadradas": 1.19599,
        "hectareas": 0.0001,
        "acres": 0.000247105
    }
    
    # 3. Convertir números a nombres de unidad si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]
    
    # 4. Validaciones
    if unidad_inicial not in factores_por_m2:
        raise ValueError(f"Unidad inicial '{unidad_inicial}' no válida.")
    if unidad_final not in factores_por_m2:
        raise ValueError(f"Unidad final '{unidad_final}' no válida.")
    
    # 5. Si las unidades son iguales, devolver la cantidad sin cambio
    if unidad_inicial == unidad_final:
        return cantidad
    
    # 6. Cálculo con conversión dinámica
    factor_origen = factores_por_m2[unidad_inicial]
    factor_destino = factores_por_m2[unidad_final]
    factor_conversion = factor_destino / factor_origen
    
    return cantidad * factor_conversion