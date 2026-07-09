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

def validar_categoria(categoria):
    """ tengo que ver la categria tenga texto de lo mismo cual sea pero que no ese vaica porque sino queda en el diccionaro"""
    if len(categoria.strip()) > 0:
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
    if multi_str.lower() == "si" or multi_str.lower() == "no":
        return True
    return False

def validar_desarrolladora(desarrolladora):
    """ tengo que hacer que ponga el estudio qeu programo el juego y no dejar vacio esto tampoco """
    if len(desarrolladora.strip()) > 0:
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

def buscar_codigo(codigo, dicc_juegos):
    """ esta funsion es para que actualizar_precio pueda revisar si el codgo del juego exite o no """
    if codigo in dicc_juegos:
        return True
    return False

def obtener_plataformas_actuales(dicc_juegos):
    """ creo una lista vasia que recorre el diccionario con un For saco la ptaforma de cada juego y tengo que usar el append para guardarla y le mmeto un if oara que no serepitan las consolas en la llista"""
    lista_plataformas = []
    for cod, datos in dicc_juegos.items():
        plat_juego = datos[1] # tengo la plataforma en la posicion 1 

        if plat_juego not in lista_plataformas:
            lista_plataformas.append(plat_juego)
            
    return lista_plataformas

def leer_opcion():
    """ aqui tengo que usar bien el try porque si el usuario es medio pavo y mete una letra con el int se cae y rompe mi programa completo por eso tengo qeu usar un execpt """
    try:
        opcion = int(input("seleccione una opcion (1-6): "))
        return opcion
    except:
        print("Error: Tienes que ingresar un número entero.")
        return 0

def stock_plataforma(dicc_juego, dicc_inventario):
    """ aqui tengo que pedirle al la consola que recorra los juegos y ir sumando el stock de las copias y mostrar el total al final """
    plat = input("ingrese la ptataforma (pc, Switch, PS5, Xbox): ")
    if not validar_plataforma(plat):
        print("Esa plataforma no es válida.")
        return

    total_stock = 0
    encontrado = False

    # tengo que pillar que juego son de las colsolas elegidas

    for cod, datos in dicc_juego.items():
        if datos[1] == plat:
            encontrado = True
            # tiene que guardar el stock en el otro diccionario en la posison 1
            cantidad = dicc_inventario[cod][1]
            total_stock += cantidad

    if encontrado: 
        print("=======================================")
        print("El stock total para " + plat + " es:" + str(total_stock) + "unidades.")
        print("======================================")
    else:
        print("No hay juegos registrado para esta plataforma" + plat)
    
def busqueda_precio(dicc_juegos, dicc_inventario):
    """tengo que hacer la busqueda de presio y el que se filtre solo los qeu tengan stock """
    try:
        minimo = int(input("ingrese el precio minimo: "))
        maximo = int(input("ingrese el precio maximo: "))
    except:
        print("coloque solo numeros validos para los precios.")
        return    

    if minimo > maximo:
        print("El minimo no puede ser mayor que el maximo.")    
        return
    # tengo que hacer la lista par meter los nombres u poder ordenar facil 
    lista_nombres = []

    for cod, datos_inv in dicc_inventario.items():
        precio = datos_inv[0]
        stock = datos_inv[1]

    # tengo que validar si esta en el precio y queda en stock 

        if precio >= minimo and precio <= maximo and stock > 0:
         datos_juego = dicc_juegos[cod]
         nombre_juego = datos_juego[0]
         lista_nombres.append(nombre_juego)

    # hare que se vea mas ordenado aplicando un orden alfavetico     
    lista_nombres.sort()

    if len(lista_nombres) >0:
        print("\n--- JUEGOS ENCONTRADOS DISPONIBLES ---")
        for nom in lista_nombres:
            print("- "+ nom)
        print("----------------------------------------")
    else:
        print("No se a encontrado juegos con stock en ese rango de precios. ")

def actualizar_precio(dicc_juegos, dicc_inventario):
    """ tiene que buscar el codigo para poder cambiar el precio  y tengo que usar un while por si quiere seguir cambiado mas precios de una """
    continuar = "si"
    while continuar.lower() == "si":
        cod = input("Ingrese el codigo del juego a acualizar (ej: GOO1): ")

        if buscar_codigo(cod, dicc_juegos):
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio para el juego; "))
                if validar_precio(nuevo_precio): # ahora con la posision 0 es el precio a cambiar de una 
                    dicc_inventario[cod][0] = nuevo_precio
                    print("Precio actualizado correctamente para el juego: " + dicc_juegos[cod][0])
                else:
                    print("Precio invalido. Tiene que ser mayor a 0.")
            except:
                print("Erroe: El precio debe ser un número entero.")
        else:
            print("El codigo de juego no existe en el sistema o esta mal escrito ") 

        continuar = input("¿Desea actualizar otro precio? (si/no); ")

def agregar_juego(dicc_juegos, dicc_inventario):
    """ tengo que hacer que pida todos los datos pero ir validando uno por uno y si una pura cuestion falla chao se frena la ejecusion y no deberia de guardar nada"""
    print("\n--- REGISTRAR NUEVO JUEGO ---")

    while True:
    
     cod = input("codigo (ej: G007):")
     if buscar_codigo(cod, dicc_juegos):
        print("Error: este codigo ya existe.")
        return
    
     if not validar_codigo(cod):
         print("Error: Codigo con formato incorrecto.")
         return

     nom = input("Nombre del videjuego: ")
     if not validar_nombre(nom):
         print("Error: El nombre no puede estar vacio.")
         return

     plat = input("plataforma (PC, Switch, PS5, Xbox): ")
     if not validar_plataforma(plat):
         print("Error: La plataforma no es valida")    
         return
    
     cat = input("categoria/genreo: ")
     if not validar_categoria(cat):
         print("Error: Ctegoria no es valida. ")
         return

     clas = input("Clasificacion (E, T, M, E10+): ")
     if not validar_clasificacion(clas):
         print("Error: Clasificacion no es valida")
         return

     multi_str = input("¿es Multijufgador? (si/no). ")
     if not validar_multijugador(multi_str):
         print("Error: Responda si o no. ")
         return

     des = input("Desarrolladora / Estudio: ")
     if not validar_desarrolladora(des):
         print("Error: la desarrolladora no puede estar vacia.")
         return

     try:
         prec = int(input("Precio del juego: "))
         if not validar_precio(prec):
              print("Error: El precio debe ser mayor a 0. ")
              return

     except:
         print("Error: El precio debe ser un numero entero: ")
         return

     try:
         stk = int(input("Stock inicial: "))
         if not validar_stock(stk):
            print("Error: El stock no puede sr negativo.") 
            return
     except:
         print("Error: el stock debe ser un numero entero: ")
         return

     # si llegue aqui todod deveria de fucnionar si no mi SI/NO o mi True/False estan mal o esscribi algo mal 

     if multi_str.lower() == "si":
        multi_bool = True
     else:
        multi_bool = False  

     # tengo qeu hacer que los datos esten ordenaditos a los dos diccionarios usando la misma clave

     dicc_juegos[cod] = [nom, plat, cat.lower(), clas,multi_bool, des]
     dicc_inventario[cod] = [prec, stk]
     
     print("¡juego guardado con exito en el sistema!")
     break

def eliminar_juego(dicc_juegos, dicc_inventario):
    """ tengo que sacar el juego del mapa asi que lo tengoque lograr borrarlo de los dos dicicionaros al mismo tiempo usando pop para qeu no queden datos guachos por hai """ 

    cod = input("Ingrese el codigo del juego que desea eliminar: ")

    if buscar_codigo(cod, dicc_juegos):
        dicc_juegos.pop(cod)
        dicc_inventario.pop(cod)
        print("El juego con codigo" + cod + " fue eliminado completamente ")
    else:
        print("No se encontro ningun juego con ese codigo. ")

#=========================
#   MENU DE LA TIENDA
#=========================        
""" LOGRE crear los dos diccionarios relacionandos y tengo qeu implementar el uso del while ordenado para inpmlementar con el for para tomar una condicion de ejecucion """
# tengo que llamar a la funcion nueva antes de empezar el menu para que carge la lista 
plataformas_en_tienda = obtener_plataformas_actuales(juegos)

ejecutando = True

while ejecutando:
    # menu para la tienda y los juegos 

    print("\n ==== MENU PRINCIPAL====")
    print("1. Stock por plataforma")
    print("2. busqueda de juegos por rango de precio")
    print("3. atualiar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6 salir")

    opc = leer_opcion()

    # tengo que hacer las funciones para que me derive cada una segun el nu,ero que ponga 
    if opc == 1:
        stock_plataforma(juegos, inventario)
    elif opc == 2:
        busqueda_precio(juegos, inventario)
    elif opc == 3:
        actualizar_precio(juegos, inventario)
    elif opc == 4:
        agregar_juego(juegos, inventario)
        # quiero qeu al agragar un juego poder voler a acaualizar la lista por si ingreso una nueva consola     
        plataformas_en_tienda = obtener_plataformas_actuales(juegos)
    elif opc == 5:
        eliminar_juego(juegos, inventario)
        # si borro un juego tiene que actualzar la lista tambin si se borro el unico que quedaba 
        plataformas_en_tienda = obtener_plataformas_actuales(juegos)
    elif opc == 6:
        print("Saliendo del programa... ¡chao!")
        ejecutando = False
    else:
        print("Opcion invalida, intenta con un numero del 1 al 6 ")
