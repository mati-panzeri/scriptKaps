#Funcion para limpiar saltos de linea
def cleanNewLine (frame):
    return list(map(lambda l: l.rstrip('\n'), frame))
