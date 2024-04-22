from random import randint



def verificar_float(monto, mensaje):
    while True:
        try:
            monto = float(input(mensaje))
            monto = float(format(monto, ".2f"))
            if monto > 0: 
                return monto
            else:
                print('Introduce un valor flotante o entero')
        except:
            print('Introduce un valor flotante o entero')

def depositar(usuario_saldo):
        deposito = 0
        deposito = verificar_float(deposito, 'Introduce el monto a depositar: ')
        usuario_saldo += deposito
        return (usuario_saldo)



def retirar(usuario_saldo):
        retiro = 0
        retiro = verificar_float(retiro, 'Introduce el monto a retirar: ')
        if usuario_saldo > retiro:
            usuario_saldo -= retiro
            return usuario_saldo
        else:
            print('Fondo insuficiente')
            return usuario_saldo
        

class Persona:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        


class Usuario(Persona):

    def __init__(self, nombre, apellido, cedula, nombre_usuario, contrasena):

        super().__init__(nombre, apellido, cedula)

        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.cuenta = []
        self.saldo = 0

        


class Sistema_Bancario:

    def __init__(self):
        self.usuarios = [Ryan, john]
        self.sesion = ''

    def menu_de_iniciar_sesion(self):
         while True:

            print('1- Iniciar sesion')
            print('2- Salir')

            opcion = input('introduce una opcion: ')

            if opcion == '1':
                print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                
                verificar = False
                comprobar_nombre = input('1- Introduce el nombre del usuario: ')
                comprobar_contrasena = input('2- Introduce la contrasena: ')
                for usuario in self.usuarios:
                    if usuario.nombre_usuario == comprobar_nombre and usuario.contrasena == comprobar_contrasena:
                        self.sesion = usuario.cedula
                        sistema1.menu_de_usuario()
                        verificar = True
                if verificar == False:
                    print('Nombre de usuario o contrasena incorrecta')
               
                    
                print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')


            elif opcion == '2':
                print('Saliendo del programa...')
                break

            else:
                print('Introduce una opcion entre 1 y 2')


      

    def menu_de_usuario(self):
        while True:

            for usuario in self.usuarios:
                    if usuario.cedula == self.sesion:
                        usuario_en_sesion = usuario

            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('1- Crear cuenta bancaria')
            print('2- Depositar')
            print('3- Retirar')
            print('4- Transferir')
            print('5- Fondos de Cuenta')
            print('6- Cerrar sesion')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')

            opcion = input('introduce una opcion: ')

            if opcion == '1':
                
                if len(usuario_en_sesion.cuenta) == 0:

                    numero_de_cuenta = ''.join([str(randint(1,10)) for n in range(11)])
                    print('Tu cuenta Bancaria es:', numero_de_cuenta)

                    saldo = 0
                    saldo = verificar_float(saldo, 'introduce un saldo: ')
                    usuario_en_sesion.cuenta = numero_de_cuenta
                    usuario_en_sesion.saldo = saldo
                  
                else:
                    print('Ya posees un cuenta')
        
    

            elif opcion == '2':

                usuario_en_sesion.saldo = depositar(usuario_en_sesion.saldo)

            elif opcion == '3':

                usuario_en_sesion.saldo = retirar(usuario_en_sesion.saldo)
                
            elif opcion == '4':
                
                u = True
                verificar = False
                transferir = 0
                
                while u == True:
                    cedula = input('Introduce la cedula de la persona a transferir: ')
                    for usuario in self.usuarios:
                            if usuario.cedula == cedula and usuario_en_sesion.cedula != cedula:
                                print('Se realizara la Transferencia al siguiente numero de cuenta:', usuario.cuenta)
                                transferir = verificar_float(transferir, 'Introduce el monto a transferir: ')
                                if usuario_en_sesion.saldo > transferir:
                                    usuario_en_sesion.saldo > transferir
                                    usuario.saldo += transferir
                                    usuario_en_sesion.saldo -= transferir
                                    print('Transferencia exitosa')
                                    u = False
                                    verificar = True
                                else:
                                    print('fondo insuficiente')

                    if verificar == False:
                        print('Cedula incorrecta')

            elif opcion == '5':
        
                print('Nombre:', usuario_en_sesion.nombre)
                print('Apellido:', usuario_en_sesion.apellido)
                print('Cedula', usuario_en_sesion.cedula)
                if len(usuario_en_sesion.cuenta) > 0:
                    print('Numero de cuenta:', usuario_en_sesion.cuenta)
                    print('Saldo:', usuario_en_sesion.saldo)
                else:
                    print('Numero de cuenta y saldo no creados')
                

            elif opcion == '6':
                self.sesion = ''
                break

            else:
                print('Introduce una opcion entre 1 y 6')

            

Ryan = Usuario('Ryan', 'Smith', '25333444', 'ryansmith', '1234')
john = Usuario('John', 'Doe', '26275576', 'johndoe', '1234')


sistema1 = Sistema_Bancario()
sistema1.menu_de_iniciar_sesion()


