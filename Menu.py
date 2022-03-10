
class Menu1:

    def __init__(self):
        print('======Bienvenido======')

    def Principal(self):

        salir = False

        while salir ==False:
            #presentacion de opciones: 
            print('|| Elija una opcion:  -----------------||')
            print('|| 1. Agregar una nueva orden.         ||')
            print('|| 2. Ver Ordenes en cola.             ||')
            print('|| 3. Mostrar datos del desarrollador. ||')
            print('|| 4. Salir.                           ||')
            print('||-------------------------------------||')
            eleccion = int(input()) #ingreso de opciones

            if eleccion == 1:
                print('Opcion Numero 1:')

                self.Secundario()

            elif eleccion == 2:
                print('Opcion Numero 2:')

            elif eleccion == 3:
                print('Opcion Numero 3:')

            elif eleccion == 4:
                print('Opcion Numero 4:')
                print('Saliendo del programa...')

                salir =True

            else:
                print('Opcion ingresada invalida,vuelva a intruducir su eleccion.')

    def Secundario(self):

        salir = False

        while salir == False:

            print('|| Ingrese los Datos del Cliente:           ||')

            print('|| Ingrese el nombre:                       ||')

            nombre = input() 

            print('|| Ingrese el nit:                          ||')

            nit = input()

            print('|| Ingrese la orden:                        ||')

            salir2 = False

            while salir2 == False:

                print('||  Ingredie Pizza      Tiempo estimado ||')
                print('------------------------------------------')
                print('|| 1. Pepperoni             3 minutos   ||')
                print('|| 2. Pepperoni             4 minutos   ||')
                print('|| 3. Pepperoni            10 minutos   ||')
                print('|| 4. Pepperoni             5 minutos   ||')
                print('|| 5. Pepperoni             2 minutos   ||')
                print('------------------------------------------')

                opcion = int(input())

                print('|| Desea agregar otra pizza?            ||')
                print('||    1. Si              2. No          ||')

                agregar = int(input())

                if agregar == 1:
                    continue
                elif agregar == 2:
                    salir2 =True
                    salir = True
                    
                else:
                    print(' NO INGRESO UNA OPCION VALIDA!')


                




