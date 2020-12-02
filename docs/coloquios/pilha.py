class Pilha:
    pilha = list()

    def __init__(self, elemento=None):
        if elemento:
            self.inserir(elemento)

    def inserir(self, elemento):
        self.pilha.insert(0, elemento)

    def remover(self):
        elemento = self.pilha.pop(-1)
        return elemento

    def tamanho(self):
        contador = 0
        for elemento in self.pilha:
            contador += 1
        return contador

    def vazia(self):
        return self.tamanho() == 0

    def topo(self):
        return self.pilha[-1]
