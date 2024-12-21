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

def go_to(actual_page, function):
    actual_page.destroy()
    function()