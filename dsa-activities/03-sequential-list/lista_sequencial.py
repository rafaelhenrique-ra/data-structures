class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.lista = [None] * capacidade
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def esta_cheia(self):
        return self.tamanho == self.capacidade

    def obter_tamanho(self):
        return self.tamanho

    def obter_elemento(self, posicao):
        if 1 <= posicao <= self.tamanho:
            return self.lista[posicao - 1]
        raise IndexError("Posição inválida")

    def modificar_elemento(self, posicao, valor):
        if 1 <= posicao <= self.tamanho:
            self.lista[posicao - 1] = valor
        else:
            raise IndexError("Posição inválida")

    def inserir(self, posicao, valor):
        if self.esta_cheia():
            raise Exception("Lista cheia")
        if not 1 <= posicao <= self.tamanho + 1:
            raise IndexError("Posição inválida")

        for i in range(self.tamanho, posicao - 1, -1):
            self.lista[i] = self.lista[i - 1]
        
        self.lista[posicao - 1] = valor
        self.tamanho += 1

    def remover(self, posicao):
        if self.esta_vazia():
            raise Exception("Lista vazia")
        if not 1 <= posicao <= self.tamanho:
            raise IndexError("Posição inválida")

        elemento_removido = self.lista[posicao - 1]
        
        for i in range(posicao - 1, self.tamanho - 1):
            self.lista[i] = self.lista[i + 1]
        
        self.lista[self.tamanho - 1] = None
        self.tamanho -= 1
        return elemento_removido

    def __str__(self):
        return str([x for x in self.lista if x is not None])


def testar_lista():
    lista = ListaSequencial(5)
    
    print("Lista vazia:", lista.esta_vazia())
    print("Lista cheia:", lista.esta_cheia())
    print("Tamanho:", lista.obter_tamanho())
    
    lista.inserir(1, 10)
    lista.inserir(1, 20)
    lista.inserir(2, 30)
    
    print("\nApós inserções:")
    print("Lista:", lista)
    print("Tamanho:", lista.obter_tamanho())
    print("Elemento na posição 2:", lista.obter_elemento(2))
    
    lista.modificar_elemento(2, 50)
    print("\nApós modificar posição 2:")
    print("Lista:", lista)
    
    removido = lista.remover(1)
    print("\nElemento removido:", removido)
    print("Lista após remoção:", lista)
    
    try:
        lista.inserir(10, 100)
    except Exception as e:
        print("\nErro ao inserir:", e)
    
    try:
        lista.remover(10)
    except Exception as e:
        print("Erro ao remover:", e)

    print("\nEstado final:")
    print("Lista vazia:", lista.esta_vazia())
    print("Lista cheia:", lista.esta_cheia())
    print("Tamanho:", lista.obter_tamanho())
    print("Lista:", lista)


if __name__ == "__main__":
    testar_lista()