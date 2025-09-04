from stack import Stack

def editor_texto(N, operaciones):
    cadena = " " 
    historial = Stack()

    for i in range(1,N):
        op = operaciones[i]

        if op == "append":
            pass
