class FilaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.tamanho = 0
        self.elementos = [None] * capacidade

    def inserir(self, valor):
        if self.cheia():
            raise Exception("Fila cheia")
        
        self.fim = (self.fim + 1) % self.capacidade
        self.elementos[self.fim] = valor
        self.tamanho += 1

    def remover(self):
        if self.vazia():
            raise Exception("Fila vazia")
        
        valor = self.elementos[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return valor

    def consultar_inicio(self):
        if self.vazia():
            raise Exception("Fila vazia")
        return self.elementos[self.inicio]

    def vazia(self):
        return self.tamanho == 0

    def cheia(self):
        return self.tamanho == self.capacidade

    def __str__(self):
        if self.vazia():
            return "[]"
        
        elementos_str = []
        indice = self.inicio
        for _ in range(self.tamanho):
            elementos_str.append(str(self.elementos[indice]))
            indice = (indice + 1) % self.capacidade
        
        return "[" + ", ".join(elementos_str) + "]"


def main():
    fila = FilaSequencial(5)
    
    print("Fila vazia?", fila.vazia())
    
    fila.inserir(10)
    fila.inserir(20)
    fila.inserir(30)
    print("Fila após inserções:", fila) 
    
    print("Início da fila:", fila.consultar_inicio())
    
    removido = fila.remover()
    print("Elemento removido:", removido)
    print("Fila após remoção:", fila)
    
    fila.inserir(40)
    fila.inserir(50)
    fila.inserir(60)
    print("Fila cheia?", fila.cheia())
    
    try:
        fila.inserir(70) 
    except Exception as e:
        print(e) 
    
    fila.remover() 
    fila.inserir(70)
    print("Fila após operações circulares:", fila)

if __name__ == "__main__":
    main()