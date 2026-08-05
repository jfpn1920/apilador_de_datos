import random
ids = []
nombres = []
descripciones = []
categorias = []
prioridades = []
estados = []
fechas = []
observaciones = []
#--------------------------------------#
#--|menu_principal_apilador_de_datos|--#
#--------------------------------------#
while True:
    print("menu principal apilador de datos")
    print("1) apilar dato")
    print("2) editar dato")
    print("3) desapilar dato")
    print("4) buscar dato")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------#
    #--|apilar_dato|--#
    #-----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_dato = 1
        else:
            id_dato = ids[-1] + 1
        nombre = input("nombre del dato: ")
        descripcion = input("descripción: ")
        categoria = input("categoría: ")
        prioridad = input("prioridad (alta, media o baja): ")
        estado = input("estado (activo o inactivo): ")
        fecha = input("fecha de registro: ")
        observacion = input("observación: ")
        ids.append(id_dato)
        nombres.append(nombre)
        descripciones.append(descripcion)
        categorias.append(categoria)
        prioridades.append(prioridad)
        estados.append(estado)
        fechas.append(fecha)
        observaciones.append(observacion)
        print("dato apilado correctamente.")
        print("id:", id_dato)
    #-----------------#
    #--|editar_dato|--#
    #-----------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            print("editar dato")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del dato: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {descripciones[posicion]}")
                nombres[posicion] = input("nuevo nombre: ")
                descripciones[posicion] = input("nueva descripción: ")
                categorias[posicion] = input("nueva categoría: ")
                prioridades[posicion] = input("nueva prioridad: ")
                estados[posicion] = input("nuevo estado: ")
                fechas[posicion] = input("nueva fecha: ")
                observaciones[posicion] = input("nueva observación: ")
                print("dato actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|desapilar_dato|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            posicion = len(ids) - 1
            print("último dato de la pila")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("descripción:", descripciones[posicion])
            print("categoría:", categorias[posicion])
            print("prioridad:", prioridades[posicion])
            print("estado:", estados[posicion])
            print("fecha:", fechas[posicion])
            print("observación:", observaciones[posicion])
            respuesta = input("¿desea desapilar este dato? (s/n): ")
            if respuesta.upper() == "S":
                ids.pop()
                nombres.pop()
                descripciones.pop()
                categorias.pop()
                prioridades.pop()
                estados.pop()
                fechas.pop()
                observaciones.pop()
                print("dato desapilado correctamente.")
            else:
                print("el dato no fue eliminado.")
    #-----------------#
    #--|buscar_dato|--#
    #-----------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            print("buscar dato")
            id_buscar = int(input("ingrese la id del dato: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("descripción:", descripciones[posicion])
                print("categoría:", categorias[posicion])
                print("prioridad:", prioridades[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            activos = 0
            inactivos = 0
            prioridad_alta = 0
            prioridad_media = 0
            prioridad_baja = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {estados[i]}")
                if estados[i].lower() == "activo":
                    activos += 1
                elif estados[i].lower() == "inactivo":
                    inactivos += 1
                if prioridades[i].lower() == "alta":
                    prioridad_alta += 1
                elif prioridades[i].lower() == "media":
                    prioridad_media += 1
                elif prioridades[i].lower() == "baja":
                    prioridad_baja += 1
            print("estadísticas apilador de datos")
            print("cantidad de datos:", len(ids))
            print("activos:", activos)
            print("inactivos:", inactivos)
            print("prioridad alta:", prioridad_alta)
            print("prioridad media:", prioridad_media)
            print("prioridad baja:", prioridad_baja)
            posicion = len(ids) - 1
            print("dato en la parte superior de la pila")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("descripción:", descripciones[posicion])
            print("categoría:", categorias[posicion])
            print("prioridad:", prioridades[posicion])
            print("estado:", estados[posicion])
            print("fecha:", fechas[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el apilador de datos.")
        break
    else:
        print("opción no válida.")