from stack import Stack

def cadena_de_profundidad(cadena):
    pila = Stack()
    maxima_profundidad = 0
    numero_en_max = None


    for i in cadena:
        if i == "(":
            pila.push("(")

        elif i == ")":
            if pila.len() == 0 :
                return "pila vacia"
            pila.pop()

        elif i.isdigit():
            profundidad_actual = pila.len()
            if profundidad_actual > maxima_profundidad:
                maxima_profundidad = profundidad_actual
                numero_en_max = i



    return maxima_profundidad, numero_en_max


print(cadena_de_profundidad("(1)+((2))+(((3)))"))
print(cadena_de_profundidad("(1+(2*3)+((8)/4))+1"))
print(cadena_de_profundidad("((((((((1+(2*3)+((((((((((((8))))))))/4))+1"))