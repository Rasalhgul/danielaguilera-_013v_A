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
    """si no escribo tal cual algunas de estas consolas porque si pongo ' plya5' y no 'PS5' fallla la busqueda despues"""
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

def validar_precio(precio_num):
    """ el precio no puede ser gratis ni meos que sero o si no la tienda pierde plata asi qeu tengo que hacer una restriccion mayora cero sino me despiden jaja"""
    if precio_num > 0:
        return True
    return False    

def validar_stock(stock_num):
    """ tengo que hacer el stock es cero por si queda no quedan en stock """
    if stock_num >= 0:
        return True
    return False

#=======================
# FUNCIONES DEL PROGRAMA
#=======================

def obtener_plataformas_actuales(dicc_juegos):
    """ creo una lista vasia que recorre el diccionario con un For saco la ptaforma de cada juego y tengo que usar el append para guardarla y le mmeto un if oara que no serepitan las consolas en la llista"""
    lista_plataformas = []
    for cod, datos in dicc_juegos.items():
        plat_juego = datos[1] # tengo la plataforma en la posicion 1 

        if plat_juego not in lista_plataformas:
            lista_plataformas.append(plat_juego)
            
    return lista_plataformas

def leer_opcion():
    """ aqui tengo que usar vien el try porque si el usuario es medio pavo y mete una letra con el int se cae y rompe mi programa completo por eso tengo qeu usar un execpt """
    