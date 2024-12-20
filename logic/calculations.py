# Lógica para cálculos de promedios

def calcular_promedio_materia(notas):
    """
    Recibe una lista de notas y devuelve el promedio.
    """
    if notas:
        return sum(notas) / len(notas)
    return 0.0

def calcular_promedio_semestre(materias):
    if materias:
        promedios = [calcular_promedio_materia(m['notas']) for m in materias]
        return sum(promedios) / len(promedios)
    return 0.0
