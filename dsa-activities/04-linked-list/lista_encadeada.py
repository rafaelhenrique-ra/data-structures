class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self._size = 0

    def esta_vazia(self):
        return self.head is None

    def obter_tamanho(self):
        return self._size

    def _obter_no(self, posicao):
        if not 1 <= posicao <= self.obter_tamanho():
            raise IndexError("Posição inválida na lista.")
        
        ptr = self.head
        for _ in range(posicao - 1):
            if ptr:
                ptr = ptr.next
            else:
                raise IndexError("Posição inválida na lista.")
        return ptr

    def obter_valor(self, posicao):
        no = self._obter_no(posicao)
        if no:
            return no.data
        raise IndexError("Posição inválida na lista.")

    def modificar_valor(self, posicao, valor):
        no = self._obter_no(posicao)
        if no:
            no.data = valor
        else:
            raise IndexError("Posição inválida na lista.")

    def inserir(self, posicao, valor):
        if not 1 <= posicao <= self.obter_tamanho() + 1:
            raise IndexError("Posição de inserção inválida.")

        novo_no = Node(valor)
        if posicao == 1:
            novo_no.next = self.head
            self.head = novo_no
        else:
            no_anterior = self._obter_no(posicao - 1)
            novo_no.next = no_anterior.next
            no_anterior.next = novo_no
        
        self._size += 1

    def retirar(self, posicao):
        if self.esta_vazia():
            raise IndexError("A lista está vazia.")

        if not 1 <= posicao <= self.obter_tamanho():
            raise IndexError("Posição de remoção inválida.")
        
        valor_removido = None
        if posicao == 1:
            valor_removido = self.head.data
            self.head = self.head.next
        else:
            no_anterior = self._obter_no(posicao - 1)
            no_a_remover = no_anterior.next
            valor_removido = no_a_remover.data
            no_anterior.next = no_a_remover.next

        self._size -= 1
        return valor_removido

    def imprimir_lista(self):
        if self.esta_vazia():
            print("Lista Vazia")
            return

        elementos = []
        ptr = self.head
        while ptr:
            elementos.append(str(ptr.data))
            ptr = ptr.next
        print(" -> ".join(elementos))