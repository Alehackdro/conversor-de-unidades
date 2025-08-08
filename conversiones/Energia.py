def convertir_energia(unidad_inicial, unidad_final, cantidad):
    """
    Convierte energías entre diferentes unidades.
    
    Args:
        unidad_inicial: Número de unidad inicial (1-8) o nombre de unidad
        unidad_final: Número de unidad final (1-8) o nombre de unidad
        cantidad: Valor de energía a convertir
    
    Returns:
        float: Energía convertida
    """
    
    # 1. Mapeo de números a nombres
    unidades = {
        "1": "joules",
        "2": "calorias",
        "3": "kilocalorias",
        "4": "electronvolts",
        "5": "kilojoules",
        "6": "btu",
        "7": "vatios_hora",
        "8": "kilovatios_hora"
    }
    
    # 2. Factores hacia joules (unidad base)
    factores_por_joule = {
        "joules": 1.0,
        "calorias": 0.239006,
        "kilocalorias": 0.000239006,
        "electronvolts": 6.242e+18,
        "kilojoules": 0.001,
        "btu": 0.000947817,
        "vatios_hora": 0.000277778,
        "kilovatios_hora": 2.77778e-7
    }
    
    # 3. Convertir números a nombres de unidad si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]
    
    # 4. Validaciones
    if unidad_inicial not in factores_por_joule:
        raise ValueError(f"Unidad inicial '{unidad_inicial}' no válida.")
    if unidad_final not in factores_por_joule:
        raise ValueError(f"Unidad final '{unidad_final}' no válida.")
    
    # 5. Si las unidades son iguales, devolver la cantidad sin cambio
    if unidad_inicial == unidad_final:
        return cantidad
    
    # 6. Cálculo con conversión dinámica
    factor_origen = factores_por_joule[unidad_inicial]
    factor_destino = factores_por_joule[unidad_final]
    factor_conversion = factor_destino / factor_origen
    
    return cantidad * factor_conversion