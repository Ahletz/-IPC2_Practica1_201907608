from xml.etree import ElementInclude
from LinkedList import*


class Menu1:


    def __init__(self):
        print('======Bienvenido======')

    def Principal(self):
        #presentacion de opciones: 
        print('|| Elija una opcion:  -----------------||')
        print('|| 1. Agregar una nueva orden.         ||')
        print('|| 2. Ver Ordenes en cola.             ||')
        print('|| 3. Eliminar Ordene en cola.         ||')
        print('|| 4. Mostrar datos del desarrollador. ||')
        print('|| 5. Salir.                           ||')
        print('||-------------------------------------||\n')
            

    def Datos_Cliente_Nombre(self):

        print('||------------------------------------------||')
        print('|| Ingrese los Datos del Cliente:           ||')
        print('||------------------------------------------||')
        print('|| Ingrese el nombre:                       ||\n')
        


    def Orden(self):

        print('||------------------------------------------||')
        print('|| Ingrese la orden:                        ||')
        print('||------------------------------------------||')
        print('||--------------------------------------||')
        print('||  Ingredie Pizza      Tiempo estimado ||')
        print('------------------------------------------')
        print('|| 1. Pepperoni             3 minutos   ||')
        print('|| 2. Salchicha             4 minutos   ||')
        print('|| 3. Carne                10 minutos   ||')
        print('|| 4. Queso                 5 minutos   ||')
        print('|| 5. Piña                  2 minutos   ||')
        print('------------------------------------------\n')

    def Cantidad(self):

        print('||--------------------------------------||')
        print('|| Cantidad de pizzas?                  ||')
        print('||--------------------------------------||\n')

    def Pregunta(self):

        print('||--------------------------------------||')
        print('|| Desea agregar otra pizza?            ||')
        print('||    1. Si              2. No          ||')
        print('||--------------------------------------||\n')

    

    def Operaciones(self):

        salir = False

        tiempo = datetime.now()
        hora = tiempo.hour
        minutos = tiempo.minute 

        llamado = Lista() #llamado a clases listas

        while salir == False:

        
            self.Principal() #llamado del primer menu 

            eleccion = int(input())
        
            if eleccion == 1:

                self.Datos_Cliente_Nombre() #nombre del cliente 

                nombre = input() #nombre del cliente

                #comienzo de programa para obtener los datos de la orden 

                salida = False 
                while salida == False:

                    self.Orden()

                    #ingrediente de la orden 

                    correcto = False

                    while correcto == False:

                        opcion = int(input())

                        if opcion == 1: 

                            ingrediente = 'Pepperoni'
                            tiempo = 3
                            correcto = True

                
                        elif opcion == 2:

                            ingrediente = 'Salchicha'
                            tiempo = 4
                            correcto = True

                        elif opcion == 3:

                            ingrediente = 'Carne'
                            tiempo = 10
                            correcto = True

                        elif opcion == 4:

                            ingrediente = 'Queso'
                            tiempo = 5
                            correcto = True

                        elif opcion == 5:

                            ingrediente = 'Piña'
                            tiempo = 2
                            correcto = True

                        else: 

                            print('INGRESO UNA OPCION NO VALIDA!')
                    
                    
                    #cantidad de pizzas a ordenar por ingrediente
                    self.Cantidad()

                    cantidad = int(input())

                    #pregunta si ordenara otra pizza
                    self.Pregunta()

                    otra = int(input())

                    #eleccion si ordena otra pizza
                    agregar = False

                    while agregar == False:

                        if otra == 1:

                            minutos += tiempo*cantidad

                            if minutos > 60:

                                minutos -= 60
                                hora +=1
                                esperah = str(hora)
                                esperam = str(minutos)
                                espera = (esperah + ':'+esperam)
                            else: 
                                esperah = str(hora)
                                esperam = str(minutos)
                                espera = (esperah + ':'+esperam)

                            llamado.Agregar(nombre,ingrediente,cantidad,tiempo,espera)
                            agregar = True

                        elif otra ==2:

                            minutos += tiempo*cantidad

                            if minutos > 60:

                                minutos -= 60
                                hora +=1
                                esperah = str(hora)
                                esperam = str(minutos)
                                espera = (esperah + ':'+esperam)
                            else: 
                                esperah = str(hora)
                                esperam = str(minutos)
                                espera = (esperah + ':'+esperam)


                            llamado.Agregar(nombre,ingrediente,cantidad,tiempo, espera)
                            salida = True
                            agregar = True

                        else:
                            print('NO INGRESO UNA OPCION VALIDA')


            elif eleccion == 2:

                llamado.Imprimir() #imprimir las colas 

            elif eleccion == 3:

                
                
                llamado.Eliminar()
                llamado.Imprimir()



            
            elif eleccion == 4:

                print('|| Nombre: Ludwwing Alexander López Ortiz     ||') #datos del desarrollador 
                print('|| Carne: 201907608                           ||')
                print('|| Carrera: Ingenieria en Ciencias y Sistemas ||\n')

            elif eleccion == 5:

                salir = True    #salir del menu 
            
            else:

                print('NO INGRESO UNA OPCION VALIDA!')



            

            



                


                




