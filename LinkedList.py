from datetime import datetime
from inspect import CO_ASYNC_GENERATOR


class Nodo:

    def __init__(self,cliente,ingrediente, cantidad,tiempo) :
        
        self.cliente = cliente
        self.ingrediente = ingrediente
        self.cantidad = cantidad
        self.tiempo = tiempo
        self.Siguiente = None

    def __str__(self):

        return str(self.cliente,self.ingrediente,self.cantidad,self.tiempo)
        

class Lista:

    def __init__(self):
        self.Primero = None
        self.Tamaño = 0

    def Agregar(self,cliente,ingrediente, cantidad, tiempo):

        Nuevo = Nodo(cliente,ingrediente, cantidad, tiempo)

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
        tiempo = datetime.now()
        hora = tiempo.hour
        minutos = tiempo.minute + puntero.tiempo

        while puntero != None:
            orden +=1
            print('|| NUMERO DE ORDEN: '+str(orden))
            print('|| '+str(hora) + ': '+str(minutos))
            print('|| cliente: '+puntero.cliente)
            print('|| Orden'+ str(puntero.cantidad) + ' '+ puntero.ingrediente)
            puntero = puntero.Siguiente
            
        print('')



        

            

        
        