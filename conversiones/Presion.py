def convertir_presion(unidad_inicial, unidad_final, cantidad):
    # 1. Mapeo de números a nombres
    unidades = {
        "1": "pascales",
        "2": "kilopascales",
        "3": "bar",
        "4": "atmosferas",
        "5": "mmhg",
        "6": "psi",
        "7": "torr",
        "8": "kgf_cm2",
        "9": "inhg",
        "10": "inh2o",
        "11": "mmh2o"
    }
    
    # 2. Factores hacia pascales (unidad base)
    factores_por_pascal = {
        "pascales": 1.0,
        "kilopascales": 0.001,
        "bar": 0.00001,
        "atmosferas": 9.8692e-6,
        "mmhg": 0.00750062,
        "psi": 0.000145038,
        "torr": 0.00750062,
        "kgf_cm2": 1.01972e-5,
        "inhg": 0.000295300,
        "inh2o": 0.00401463,
        "mmh2o": 0.101972
    }
    
    # 3. Convertir números a nombres de unidad si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]
    
    # 4. Validaciones
    if unidad_inicial not in factores_por_pascal:
        raise ValueError(f"Unidad inicial '{unidad_inicial}' no válida.")
    if unidad_final not in factores_por_pascal:
        raise ValueError(f"Unidad final '{unidad_final}' no válida.")
    
    # 5. Si las unidades son iguales, devolver la cantidad sin cambio
    if unidad_inicial == unidad_final:
        return cantidad
    
    # 6. Cálculo con conversión dinámica
    factor_origen = factores_por_pascal[unidad_inicial]
    factor_destino = factores_por_pascal[unidad_final]
    factor_conversion = factor_destino / factor_origen
    
    return cantidad * factor_conversion