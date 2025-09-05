from cola import Queue
from stack import Stack

def cafeteria(estudiantes, sanduches):

    contador_rechazos = 0 

    while not estudiantes.is_empty() and not sanduches.is_empty():

        estudiante_actual = estudiantes.dequeue()
        sanduche_actual = sanduches.top()

        if estudiante_actual == sanduche_actual:
            sanduches.pop()
            contador_rechazos = 0

        else:
            estudiantes.enqueue(estudiante_actual)
            contador_rechazos= contador_rechazos + 1

        if contador_rechazos == estudiantes.len():
            return estudiantes.len()
        
    return estudiantes.len()

    

estudiantes = Queue()
sanduches = Stack()

for i in [1,1,1,0,0,1]:
    estudiantes.enqueue(i)


for j in reversed([1,0,0,0,1,1]):
    sanduches.push(j)


resultado = cafeteria(estudiantes,sanduches)
print(resultado)