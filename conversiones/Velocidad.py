def convertir_velocidad(unidad_inicial, unidad_final, cantidad):
    # 1. Mapeo de números a nombres
    unidades = {
        "1": "m_s",
        "2": "km_h",
        "3": "mph",
        "4": "ft_s",
        "5": "nudos"
    }
    
    # 2. Factores hacia m/s (unidad base)
    factores_por_m_s = {
        "m_s": 1.0,
        "km_h": 3.6,
        "mph": 2.23694,
        "ft_s": 3.28084,
        "nudos": 1.94384
    }
    
    # 3. Convertir números a nombres de unidad si es necesario
    if unidad_inicial in unidades:
        unidad_inicial = unidades[unidad_inicial]
    if unidad_final in unidades:
        unidad_final = unidades[unidad_final]
    
    # 4. Validaciones
    if unidad_inicial not in factores_por_m_s:
        raise ValueError(f"Unidad inicial '{unidad_inicial}' no válida.")
    if unidad_final not in factores_por_m_s:
        raise ValueError(f"Unidad final '{unidad_final}' no válida.")
    
    # 5. Si las unidades son iguales, devolver la cantidad sin cambio
    if unidad_inicial == unidad_final:
        return cantidad
    
    # 6. Cálculo con conversión dinámica
    factor_origen = factores_por_m_s[unidad_inicial]
    factor_destino = factores_por_m_s[unidad_final]
    factor_conversion = factor_destino / factor_origen
    
    return cantidad * factor_conversion