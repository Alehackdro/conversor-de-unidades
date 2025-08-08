def convertir_volumen(unidad_inicial, unidad_final, cantidad):
    # 1. Mapeo opcional de números a nombres
    unidades = {
        "1": "litros",
        "2": "mililitros",
        "3": "centimetros_cubicos",
        "4": "metros_cubicos",
        "5": "galones",
        "6": "onzas_liquidas",
        "7": "pintas",
        "8": "cuartos",
        "9": "decilitros",
        "10": "hectolitros",
        "11": "microlitros",
        "12": "nanolitros",
        "13": "barriles",
        "14": "pies_cubicos",
        "15": "pulgadas_cubicas",
        "16": "yardas_cubicas"
    }

    # 2. Factores hacia litros
    factores_por_litro = {
    "litros": 1.0,
    "mililitros": 1000.0,
    "centimetros_cubicos": 1000.0,
    "metros_cubicos": 0.001,
    "decilitros": 10.0,
    "hectolitros": 0.01,
    "microlitros": 1_000_000.0,
    "nanolitros": 1_000_000_000.0,
    "galones": 0.264172,
    "cuartos": 1.05669,
    "pintas": 2.11338,
    "onzas_liquidas": 33.814,
    "barriles": 0.00628981,
    "pies_cubicos": 0.0353147,
    "pulgadas_cubicas": 61.0237,
    "yardas_cubicas": 0.00130795
    }

    # 3. Convertir números a nombres de unidad si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]

    # 4. Validaciones
    if unidad_inicial not in factores_por_litro:
        raise ValueError(f"Unidad inicial '{unidad_inicial}' no válida.")
    if unidad_final not in factores_por_litro:
        raise ValueError(f"Unidad final '{unidad_final}' no válida.")

    # 5. Si las unidades son iguales, devolver la cantidad sin cambio
    if unidad_inicial == unidad_final:
        return cantidad

    # 6. Cálculo con conversión dinámica
    factor_origen = factores_por_litro[unidad_inicial]
    factor_destino = factores_por_litro[unidad_final]
    factor_conversion = factor_destino / factor_origen

    return cantidad * factor_conversion
