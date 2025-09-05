from stack import Stack

class EditorTexto:
    def __init__(self):
        self.texto = Stack()
        self.historial = Stack()

    def append(self,s):
        for c in s:
            self.texto.push(c)
        self.historial.push(("append", s))

    def delete(self , k):
        borrados= " "
        for _ in range(k):
            borrados= self.texto.pop() + borrados
        self.historial.push(("delete", borrados))

    def print(self, k):
        aux= Stack()
        n = self.texto.len()
        char = None

        for _ in range(n):
            aux.push(self.texto.pop())

        for i in range(1, n+1):
            c = aux.pop()
            if i == k:
                char = c
            self.texto.push(c)

        return char
    

    def undo(self):
        if self.historial.is_empty():
            return
        tipo, valor = self.historial.pop()
        if tipo == "append":
            for _ in valor :
                self.texto.pop()

        elif tipo == "delete":
            for c in valor:
                self.texto.push(c)





editor = EditorTexto()
editor.append("abc")
editor.append("xy")
print(editor.print(4))
editor.delete(3)
print(editor.print(2))
editor.undo()
print(editor.print(5))
editor.undo()