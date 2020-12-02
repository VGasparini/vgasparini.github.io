class Elemento:
    dado = None
    anterior = None
    proximo = None

    def __init__(self, dado, anterior=None, proximo=None):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo


class Lista:
    cabeca = None
    cauda = None

    def __init__(self, elemento):
        self.cabeca = elemento
        self.cauda = elemento

    def inserir_no_meio(self, elemento, posicao):
        contador = 0
        elemento_atual = self.cabeca
        while (contador != posicao):
            elemento_atual = elemento_atual.proximo
            contador += 1
        elemento.proximo = elemento_atual
        elemento_atual.anterior.proximo = elemento
        elemento_atual.anterior = elemento

    def inserir_no_fim(self, elemento):
        elemento.anterior = self.cauda
        self.cauda.proximo = elemento
        self.cauda = elemento

    def inserir_no_inicio(self, elemento):
        elemento.proximo = self.cabeca
        self.cabeca.anterior = elemento
        self.cabeca = elemento
