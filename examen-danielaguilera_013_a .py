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
    if len(nombre.strip()) > 0:
        return True                    
    return False

def validar_plataforma(plataforma):
    """si no escribo tal cual algunas de estas consolas porque si pongo ' plya5' y no 'PS5' fallla la busqueda despues""""
    plataforma_validar = ["pc", "Switch", "PS5", "Xbox"]
    if plataforma in plataforma_validar:
        return True
    return False

def validar_clasificacion(clasidicacion):
    """"tengo que recordar a usar la clasificacion de escribir el E,T,M y si pongo cualquier otra cuestion va a fallarr""" 
    clasidicaciones_validas = ["E", "T", "M", "E10+"]
    if clasidicacion in clasidicaciones_validas:
        return True
    return False    

def validar_multijugador(multi_str):
    """ tengo que hacer aqui que el usuario diga si o no despues los paso a booleano si escrib otra cosa tenque mandar error altiro o queda mal """
    if multi_str.lower == "si" or multi_str.lower() == "no":
        return True
    return False

def validar_desarrolladora(desarrolladora):
    """ tengo que hacer que ponga el estudio qeu programo el juego y no dejar vacio esto tampoco """
    if len(desarrolladora.trip()) > 0:
        return True
    return False
        