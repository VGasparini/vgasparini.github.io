class Fila:
    fila = list()

    def __init__(self, elemento=None):
        if elemento:
            self.inserir(elemento)

    def inserir(self, elemento):
        self.fila.append(elemento)

    def remover(self):
        elemento = self.fila.pop(0)
        return elemento

    def tamanho(self):
        # como otimizar?
        contador = 0
        for elemento in self.fila:
            contador += 1
        return contador

    def vazia(self):
        return self.tamanho() == 0

    def frente(self):
        return self.fila[0]


if __name__ == "__main__":
    while (True):
        fila = Fila()
        cartas = int(input())
        if cartas > 0:
            for i in range(1, cartas + 1):
                fila.inserir(i)
            print("Discarded cards: ", end="")

            while (fila.tamanho() >= 2):
                if (fila.tamanho() != 2):
                    print(fila.frente(), end=", ")
                else:
                    print(fila.frente())

                fila.remover()
                fila.inserir(fila.remover())

            print("Remaining card:", fila.frente())
        else:
            break