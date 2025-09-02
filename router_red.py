from cola import Queue
class Paquete:
    def __init__(self, sourse:int, destination:int, timestamp:int):
        self.sourse = sourse
        self.destination = destination
        self.timestamp = timestamp

    def __str__(self):
        return f" Paquete: origen={self.sourse}, destino={self.destination}, tiempo={self.timestamp}"

class Router:
    def __init__(self, memory_limit = 5):
        self.cola = Queue()
        self.memory_limit = memory_limit

    def router(self, nuevo_paquete):
        if self.memory_limit == self.cola.len():
            self.cola.dequeue()
            self.cola.enqueue(nuevo_paquete)
        else:
            self.cola.enqueue(nuevo_paquete)

    def boolean_add(self, sourse:int,destination: int ,timestamp:int ):
        nuevo_paquete = Paquete(sourse, destination, timestamp)
        cola_aux = Queue()
        if self.cola.is_empty():
            self.cola.enqueue(nuevo_paquete)
            return True
        else:
            while self.cola.len() > 0:
                actual = self.cola.dequeue()
                cola_aux.enqueue(actual)
                if nuevo_paquete == actual:
                    return False
                else:
                    self.router(nuevo_paquete)
                
            
            while cola_aux.len > 0:
                self.cola.enqueue(cola_aux.dequeue())







    






paquete_1= Paquete(1,1,11)
paquete_2= Paquete(2,2,12)
paquete_3= Paquete(3,1,13)
paquete_4= Paquete(4,2,14)
paquete_5= Paquete(5,1,15)
paquete_6= Paquete(6,2,16)
paquete_7= Paquete(7,1,17)
paquete_8= Paquete(8,2,18)

rou = Router()
rou.router(paquete_1)
rou.router(paquete_2)
rou.router(paquete_3)
rou.router(paquete_4)
rou.router(paquete_5)
print("Antes: ","\n",rou.cola)
rou.router(paquete_6)
rou.router(paquete_7)
rou.router(paquete_8)
print("Despues: ","\n",rou.cola)

rou.boolean_add(9,10,11)
print(rou.cola)




