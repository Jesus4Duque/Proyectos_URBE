#Proyecro 01 Jesus Duque

listado_de_estudiantes = {}
indice = 0
s = True
t = True

while True:

    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('1- Listado de estudiantes')
    print('2- Registrar estudiante')
    print('3- Actualizar estudiante')
    print('4- Eliminar estudiante')
    print('5- Salir')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')

    seleccion = int(input('Introduce un numero: '))

    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')

    if seleccion not in (1,2,3,4,5):
        
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('Haz seleccionado una opcion invalida, intentalo de nuevo.')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    
    
    if seleccion == 1:

        if  len(listado_de_estudiantes) == 0:
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('No hay estudiantes en la lista.')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        else:
            for info_nombre, info_datos in listado_de_estudiantes.items():
                print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('El estudiante', info_datos['Nombre'].title(), info_datos['Apellido'].title(), 'de cedula:', info_datos['Cedula'], 'tiene las siguientes notas; Nota_1:', info_datos['Nota_1'], 'Nota_2:', info_datos['Nota_2'], 'Nota_3:', info_datos['Nota_3'], 'Con un Promedio de:', info_datos['Promedio'] )
                print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')


    if seleccion == 2:
        while True:
            indice += 1
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            nombre = input('Introduce el nombre del estudiante: ')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            apellido = input('Introduce el apellido del estudiante: ')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            cedula = input('Introduce la cedula del estudiante: ')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            nota_1 = input('Introduce la nota #1 del estudiante: ')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            nota_2 = input('Introduce la nota #2 del estudiante: ')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            nota_3 = input('Introduce la nota#3 del estudiante: ')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
           
        
            if len(nombre) > 0 and len(apellido) > 0 and cedula.isdigit() and nota_1.isdigit() and nota_2.isdigit() and nota_3.isdigit():

                uno = float(nota_1)
                dos = float(nota_2)
                tres = float(nota_3)   

                promedio = (uno+dos+tres) / 3
               
                listado_de_estudiantes[indice] = {'Nombre': nombre, 'Apellido': apellido, 'Cedula': cedula, 'Nota_1': nota_1, 'Nota_2': nota_2, 'Nota_3': nota_3, 'Promedio': promedio}
                print('Estudiante agregado exitosamente')
                print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                break
            else:
                print('Alguno de los datos fue incorrecto intentalo de nuevo.')
            

        
    if seleccion == 3:
       


        while s:

            c = input('Introduce la cedula del estudiante para actualizar sus datos: ')

            for i, datos_estudiante in listado_de_estudiantes.items():
                if c == listado_de_estudiantes[i]['Cedula']:
                    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    listado_de_estudiantes[i]['Nombre'] = input('Introduce el nuevo nombre para el estudiante: ')
                    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    listado_de_estudiantes[i]['Apellido'] = input('Introduce el nuevo apellido para el estudiante: ')
                    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    listado_de_estudiantes[i]['Cedula'] = input('Introduce la nueva cedula para el estudiante: ')
                    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    listado_de_estudiantes[i]['Nota_1'] = (input('Introduce la nueva nota #1 para el estudiante: '))
                    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    listado_de_estudiantes[i]['Nota_2'] = (input('Introduce la nueva nota #2 para el estudiante: '))
                    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    listado_de_estudiantes[i]['Nota_3'] = (input('Introduce la nueva nota #3 para el estudiante: '))
                    if len(listado_de_estudiantes[i]['Nombre']) > 0 and len(listado_de_estudiantes[i]['Apellido']) > 0 and  listado_de_estudiantes[i]['Cedula'].isdigit() and  listado_de_estudiantes[i]['Nota_1'].isdigit() and    listado_de_estudiantes[i]['Nota_2'].isdigit() and  listado_de_estudiantes[i]['Nota_3'].isdigit():
                        
                        uno = float(listado_de_estudiantes[i]['Nota_1'])
                        dos = float(listado_de_estudiantes[i]['Nota_2']) 
                        tres = float(listado_de_estudiantes[i]['Nota_3'])

                        listado_de_estudiantes[i]['Promedio'] = (uno + dos +tres) / 3
                        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                        print('Datos actualizados exitosamente.')
                        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                        s = False
                        break
            else:
                print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('Alguno de los datos fue incorrecto intentalo de nuevo.')
                print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                listado_de_estudiantes[i]['Cedula'] = c




    if seleccion == 4:
        while t:
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            c = input('Introduce la cedula del estudiante a eliminar: ')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            for i in listado_de_estudiantes:
                if c == listado_de_estudiantes[i]['Cedula'] and c.isdigit():
                    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    print('El estudiante', listado_de_estudiantes[i]['Nombre'], 'de cedula:', listado_de_estudiantes[i]['Cedula'], 'ha sido eliminado exitosamente.')
                    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    del listado_de_estudiantes[i]
                    t = False
                    break
            else:
                print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('Alguno de los datos fue incorrecto intentalo de nuevo.')
                print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            
            
        


    if seleccion == 5:
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('Saliendo del sistema...')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        break



