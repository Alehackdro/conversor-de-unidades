def convertir_temperatura(unidad_inicial, unidad_final, cantidad):
    """
    Convierte temperaturas entre diferentes escalas.
    
    Args:
        unidad_inicial: Número de unidad inicial (1-8) o nombre de unidad
        unidad_final: Número de unidad final (1-8) o nombre de unidad  
        cantidad: Valor de temperatura a convertir
    
    Returns:
        float: Temperatura convertida
    """
    
    # 1. Mapeo de números a nombres
    unidades = {
        "1": "celsius",
        "2": "fahrenheit", 
        "3": "kelvin",
        "4": "rankine",
        "5": "reaumur",
        "6": "delisle",
        "7": "newton",
        "8": "romer"
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
    
    # 5. Convertir primero a Celsius como unidad base
    def a_celsius(temp, unidad):
        if unidad == "celsius":
            return temp
        elif unidad == "fahrenheit":
            return (temp - 32) * 5/9
        elif unidad == "kelvin":
            return temp - 273.15
        elif unidad == "rankine":
            return (temp - 491.67) * 5/9
        elif unidad == "reaumur":
            return temp * 5/4
        elif unidad == "delisle":
            return 100 - temp * 2/3
        elif unidad == "newton":
            return temp * 100/33
        elif unidad == "romer":
            return (temp - 7.5) * 40/21
    
    # 6. Convertir de Celsius a la unidad final
    def desde_celsius(temp, unidad):
        if unidad == "celsius":
            return temp
        elif unidad == "fahrenheit":
            return temp * 9/5 + 32
        elif unidad == "kelvin":
            return temp + 273.15
        elif unidad == "rankine":
            return temp * 9/5 + 491.67
        elif unidad == "reaumur":
            return temp * 4/5
        elif unidad == "delisle":
            return (100 - temp) * 3/2
        elif unidad == "newton":
            return temp * 33/100
        elif unidad == "romer":
            return temp * 21/40 + 7.5
    
    # 7. Realizar la conversión
    temp_celsius = a_celsius(cantidad, unidad_inicial)
    resultado = desde_celsius(temp_celsius, unidad_final)
    
    return resultado