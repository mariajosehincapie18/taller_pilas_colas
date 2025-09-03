from stack import Stack
from cola import Queue


def pila_de_cola(pila_principal):
    enteros = Stack()
    entero = None

    while not pila_principal.is_empty():
        sub_pila = pila_principal.pop()

        while not sub_pila.is_empty():
            actual = sub_pila.dequeue()
            if actual % 2 == 0:
                entero = actual
        enteros.push(entero)

    return enteros



pila_principal = Stack()

cola_1 = Queue()
cola_1.enqueue(1)
cola_1.enqueue(2)
cola_1.enqueue(3)

cola_2 = Queue()
cola_2.enqueue(4)
cola_2.enqueue(5)
cola_2.enqueue(6)

cola_3 = Queue()
cola_3.enqueue(7)
cola_3.enqueue(8)
cola_3.enqueue(9)

pila_principal.push(cola_1)
pila_principal.push(cola_2)
pila_principal.push(cola_3)

print(pila_de_cola(pila_principal))











