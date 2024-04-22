from datetime import datetime
lista_de_tareas = []

def mostrar_completado():
    if len(lista_de_tareas) == 0:
        print('no hay tareas completadas registradas')
    else:
        completada = [tarea for tarea in lista_de_tareas if tarea['Status'] == 'completado']
        for tarea in completada:
            print(tarea)



def mostrar_pendiente():
    if len(lista_de_tareas) == 0:
        print('no hay tareas pendientes registradas')
    else:
        pendiente = [tarea for tarea in lista_de_tareas if tarea['Status'] == 'pendiente']
        for tarea in pendiente:
            print(tarea)
            


def validar_opcion(valor):
    while True:
        try:
            valor = int(input('introduce la opcion deseada: '))
            if valor >= 1 and valor <= 6:
                return(valor)
            else:
                print('Error introduce un numero entre 1 y 6')
        except:
            print('Error introduce un numero entre el 1 y 6')



def validar_sub_menu_1(valor):
    while True:
        try:
            valor = int(input('introduce la opcion deseada: '))
            if valor >= 1 and valor <= 3:
                return(valor)
            else:
                print('Error introduce un numero entre 1 y 3')
        except:
            print('Error introduce un numero entre el 1 y 3')      



def validar_sub_menu_2(valor):
    while True:
        try:
            valor = int(input('introduce la opcion deseada: '))
            if valor >= 1 and valor <= 4:
                return(valor)
            else:
                print('Error introduce un numero entre 1 y 4')
        except:
            print('Error introduce un numero entre el 1 y 4')    



def validar_sub_menu_4(valor):
    while True:
        try:
            valor = int(input('introduce la opcion deseada: '))
            if valor >= 1 and valor <= 6:
                return(valor)
            else:
                print('Error introduce un numero entre 1 y 6')
        except:
            print('Error introduce un numero entre el 1 y 6')          



def validar_codigo(valor, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if len(lista_de_tareas) == 0:
                return(valor)
            else:
                for tarea in lista_de_tareas:
                    if tarea['Codigo'] == valor:
                        print('Este codigo ya se ecuentra en uso, introduce uno diferente')
                    else:
                        return(valor)
        except:
            print('Introduce un codigo nuevo en valor numerico')



def validar_titulo(valor, mensaje):
    while True:
            valor = str(input(mensaje))
            if len(valor) <= 0 or len(valor) > 20:
                print('introduce un titulo entre 1 y 20 caracteres')
            else:
                return(valor)
    


def validar_descripcion(valor, mensaje):
    while True:
            valor = str(input(mensaje))
            if len(valor) <= 0:
                print('introduce una descripcion para la tarea')
            else:
                return(valor)
            

            
def validar_status(valor, mensaje):
    while True:
        valor = str(input(mensaje))
        if valor == 'completado' or valor == 'pendiente':
            return(valor)
        else:
            print('El status debe ser: completado o pendiente')


        
def validar_fecha(fecha, mensaje):
    while True:
        try:
            fecha = input(mensaje)
            datetime.strptime(fecha, '%d-%m-%Y')
            if fecha:
                return(fecha)
            else:
                print('error', mensaje)
        except:
            print('error', mensaje)



def filtrar_codigo(valor, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            for tarea in lista_de_tareas:
                if tarea['Codigo'] == valor:
                    print(tarea)
                    return valor
                else:
                    print('el codigo introducido no existe')         
        except:
            print('Introduce un numero entero y que coincida con un codigo existente')



def filtrar_titulo(valor):
    while True:
        titulo = validar_titulo(valor, 'introduce el titulo a filtrar: ')
        valor = [tarea for tarea in lista_de_tareas if tarea['Titulo'].lower().startswith(titulo)]
        for tarea in valor:
            print(tarea)
        if valor:
            return False
        else:
            print('el titulo introducido no existe')         



def filtrar_fecha(fecha, mensaje):
    while True:
        try:
            fecha = validar_fecha(fecha, 'introduce una fecha existente con el siguiente formato DD-MM-YYYY: ')
            tareas = [tarea for tarea in lista_de_tareas if tarea['Fecha'] == fecha]
            for tarea in tareas:
                print(tarea)
            if tareas:
                return False
            else:
                print('error', mensaje)
        except:
            print('error', mensaje)



def actualizar_codigo(valor, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            for tarea in lista_de_tareas:
                    if tarea['Codigo'] == valor:
                        valor = validar_codigo(valor, 'introduce un codigo nuevo para la tarea: ')
                        tarea['Codigo'] = valor
                        print('codigo actualizado exitosamente')
                        return False
                    else:
                        print('el codigo introducido no coincide con ningun codigo existente')
        except:
            print('el codigo introducido no coincide con ningun codigo existente')


                
def actualizar_titulo(valor, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            for tarea in lista_de_tareas:
                    if tarea['Codigo'] == valor:
                        valor = validar_titulo(valor, 'introduce el nuevo titulo: ')
                        tarea['Titulo'] = valor
                        print('titulo actualizado exitosamente')
                        return False
                    else:
                        print('el codigo introducido no coincide con ningun titulo existente')
        except:
            print('introduce un codigo existente para modificar la descripcion de la tarea')


def actualizar_descripcion(valor, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            for tarea in lista_de_tareas:
                if tarea['Codigo'] == valor:
                    valor = validar_descripcion(valor, 'introduce la nueva descripcion para la tarea: ')
                    tarea['Descripcion'] = valor
                    print('descripcion actualizada exitosamente')
                    return False
                else:
                    print('codigo erroneo')
        except:
            print('introduce un codigo existente para modificar la descripcion de la tarea')



def actualizar_status(valor, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            for tarea in lista_de_tareas:
                if tarea['Codigo'] == valor:
                    valor = validar_status(valor, 'introduce el nuevo status para la tarea: ')
                    tarea['Status'] = valor
                    print('status actualizado exitosamente')
                    return False
                else:
                    print('codigo erroneo')
        except:
            print('introduce un codigo existente para modificar el status de la tarea')



def actualizar_fecha(valor, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            for tarea in lista_de_tareas:
                if tarea['Codigo'] == valor:
                    valor = validar_fecha(valor, 'introduce la nueva fecha para la tarea: ')
                    tarea['Fecha'] = valor
                    print('fecha actualizada exitosamente')
                    return False
                else:
                    print('codigo erroneo')
        except:
            print('introduce un codigo existente para modificar la fecha de la tarea')



def eliminar_tarea():
    while True:
        try:
            opcion = int(input('introduce el codigo de la tarea a eliminar: '))
            for tarea in lista_de_tareas:
                if tarea['Codigo'] == opcion:
                    lista_de_tareas.remove(tarea)
                    print('tarea eliminada exitosamente')
                    return False
                else:
                    print('el codigo introducido no coincide con ninguna tarea existente')
        except:
            print('Introduce un numero entero y que coincida con un codigo existente')

while True:

    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('1- Lista de Tareas')
    print('2- Filtrar Tareas')
    print('3- Añadir Tarea')
    print('4- Actualizar Tarea')
    print('5- Eliminar Tarea')
    print('6- Salir')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    
    codigo = 0
    titulo = ''
    descripcion = ''
    status = ''
    fecha = ''
    opcion = 0
    sub_menu = 0
    validar = False
    
    
    opcion = validar_opcion(opcion)


    if opcion == 1:
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('1- Completadas')
        print('2- Pendientes')
        print('3- Atras')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        
       
        sub_menu = validar_sub_menu_1(sub_menu)

        if sub_menu == 1:
            mostrar_completado()
          

        elif sub_menu == 2:
            mostrar_pendiente()
            
        
        elif sub_menu == 3:
            continue
        

    if opcion == 2:

        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('1- Filtrar por codigo')
        print('2- Flitrar por titulo')
        print('3- Filtrar por fecha')
        print('4- Atras')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        

        sub_menu = validar_sub_menu_2(sub_menu)

        if sub_menu == 1:
            codigo = filtrar_codigo(codigo, 'introduce el codigo a filtrar: ')
        
        
        elif sub_menu == 2:
            titulo = filtrar_titulo(titulo)
            
            
        elif sub_menu == 3:
            fecha = filtrar_fecha(fecha, 'introduce la fecha con el siguiente formato: DD-MM-YYYY: ')
                

        elif sub_menu == 4:
            continue
    

    if opcion == 3:

        codigo = validar_codigo(codigo, 'introduce un codigo nuevo para la tarea: ')
        titulo = validar_titulo(titulo, 'introduce el titulo de la tarea: ')
        descripcion = validar_descripcion(descripcion, 'introduce la descripcion de la tarea: ')
        status = validar_status(status, 'introuce el status de la tarea: ')
        fecha = validar_fecha(fecha, 'introduce la fecha con el siguiente formato: DD-MM-YYYY: ')

        lista_de_tareas.append({'Codigo': codigo, 'Titulo': titulo, 'Descripcion': descripcion, 'Status': status, 'Fecha': fecha})

    if opcion == 4:
        
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('1- Actualizar codigo')
        print('2- Actualizar titulo')
        print('3- Actualizar descripcion')
        print('4- Actualizar status')
        print('5- Actualizar fecha')
        print('6- Atras')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        
        sub_menu = validar_sub_menu_4(sub_menu)

        if sub_menu == 1:
            codigo = actualizar_codigo(codigo, 'introduce el codigo que desea actualizar: ')

        elif sub_menu == 2:
            titulo = actualizar_titulo(titulo, 'introduce el codigo de la tarea para actualizar el titulo: ')
        
        elif sub_menu == 3:
            descripcion = actualizar_descripcion(descripcion, 'introduce el codigo de la tarea para actualizar la descripcion: ')

        elif sub_menu == 4:
            status = actualizar_status(status, 'introduce el codigo de la tarea para actualizar su status: ')

        elif sub_menu == 5:
            fecha = actualizar_fecha(fecha, 'introduce el codigo de la tarea para actualizar su status: ')

        elif sub_menu == 6:
            continue
        

    if opcion == 5:
        eliminar_tarea()
        
    if opcion == 6:
        print('saliendo del programa...')
        break
    


