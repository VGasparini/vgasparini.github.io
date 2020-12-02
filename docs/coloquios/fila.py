class Fila:
    fila = []

    def __init__(self, elemento=None):
        if elemento:
            self.inserir(elemento)

    def inserir(self, elemento):
        self.fila.append(elemento)

    def remover(self):
        elemento = self.fila.pop(0)
        return elemento

    def tamanho(self):
        contador = 0
        for elemento in self.fila:
            contador += 1
        return contador

    def vazia(self):
        return self.tamanho() == 0

    def frente(self):
        return self.fila[0]
