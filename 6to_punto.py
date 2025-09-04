from stack import Stack


def notacion_posfija(ecuacion):
    pila = Stack()
    operadores = "+-/*"

    for i in ecuacion:
        if i.isdigit():
            pila.push(int(i))

        elif i in operadores:
            if pila.len() >= 2:
                ultimo_digito = pila.pop()
                penultimo_digito = pila.pop()
                if i == "+":
                    operacion =penultimo_digito + ultimo_digito
                elif i == "-":
                    operacion = penultimo_digito - ultimo_digito
                elif i == "/":
                    operacion = penultimo_digito / ultimo_digito
                elif i == "*":
                    operacion = penultimo_digito * ultimo_digito
               
                pila.push(operacion)
            else:
                return "faltan valores para hacer la operacion"

        else:
            return " no es un valor valido"
        
    if pila.len() == 1:
        return pila.pop()
    else:
        "expresion invalida"


print(notacion_posfija("43+"))
print(notacion_posfija("35*83+-"))
print(notacion_posfija("62+5*31-/"))
print(notacion_posfija("745*+20+-"))