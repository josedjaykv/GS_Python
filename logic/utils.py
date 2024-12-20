# Funciones genéricas que pueden ser útiles en todo el proyecto, como validaciones.
# Funciones generales (validaciones, etc.)

def validar_numero(valor):
    """
    Valida que el valor sea un número flotante.
    """
    try:
        return float(valor)
    except ValueError:
        return None

