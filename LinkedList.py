from datetime import datetime
from graphviz import Digraph


class Nodo:

    def __init__(self,cliente,ingrediente, cantidad,tiempo, espera) :
        
        self.cliente = cliente
        self.ingrediente = ingrediente
        self.cantidad = cantidad
        self.tiempo = tiempo
        self.espera = espera
        self.Siguiente = None

    def __str__(self):

        return str(self.cliente,self.ingrediente,self.cantidad,self.tiempo,self.espera)
        

class Lista:

    def __init__(self):
        self.Primero = None
        self.Tamaño = 0

    def Agregar(self,cliente,ingrediente, cantidad, tiempo, espera):

        Nuevo = Nodo(cliente,ingrediente, cantidad, tiempo,espera)

        if self.Tamaño == 0:
            self.Primero = Nuevo
        else:
            current = self.Primero
            while current.Siguiente != None:
                current = current.Siguiente
            current.Siguiente = Nuevo
        
        self.Tamaño+=1
        return Nuevo
    
    def Imprimir(self):

        puntero = self.Primero
        orden = 0
         
        if self.Tamaño == 0:
            print('NO HAY ORDENES EN LA COLA')
        else: 

            while puntero != None:
                orden +=1
                print('|| NUMERO DE ORDEN: '+str(orden))
                print('|| cliente: '+puntero.cliente)
                print('|| Orden: '+ str(puntero.cantidad) + ' Pizzas de :'+ puntero.ingrediente)
                print('|| TIEMPO: '+ puntero.espera)
                print('\n')
                puntero = puntero.Siguiente
                
        print('')

        

    def Eliminar(self):

        puntero = self.Primero

        while puntero != None:

            self.Primero = puntero.Siguiente
            puntero = puntero.Siguiente
            





        

            

        
        