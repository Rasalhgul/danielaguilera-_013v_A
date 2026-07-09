#=====================
# DICCINORIO PRINCIPAL
#=====================
"""aqui pongo el dicionario y su categoria donde queda la infomacion del producto y su codigo""" 

juegos = {
    'G001': ['Eclipse Runner', 'pc', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'pc', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
}
"""" debe recorer el dicionario para encontrar que tiene que encontrar en la categoria con su codigo """
inventario ={
    'G001': [99990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}

#========================
# FUNCIONES DE VALIDACIÓN
#========================

def validar_codigo(codigo):
    """"aqui tengo que ver si el codigo sirve si no tiene 4 letras o numero se rompe altiro el sistema la primera letra si o si tiene que ser la G mayuscula sino falla """

    if len(codigo) !=4:
        return False
    if codigo[0] != 'G':
        return False

    numeros = codigo[1:]
    if numeros.isdigit():
        return True
    else:
        return False

def validar_nombre(nombre):
    """ aqui el usuario me deja el nombre vacio se rompe la lista asi que strip para borrar espacios y ver que tenga algoe escrito """
                        
