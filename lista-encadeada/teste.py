from lista_encadeada import ListaEncadeada

if __name__ == "__main__":
    
    print("--- 1. Criação da lista vazia ---")
    lista = ListaEncadeada()
    lista.imprimir_lista()
    print()

    print("--- 2. Verificar se a lista está vazia ---")
    print(f"A lista está vazia? {lista.esta_vazia()}")
    print()

    print("--- 3. Obter o tamanho da lista ---")
    print(f"Tamanho da lista: {lista.obter_tamanho()}")
    print()

    print("--- 5. Inserir elementos ---")
    print("Inserindo 10 na posição 1...")
    lista.inserir(1, 10)
    lista.imprimir_lista()
    
    print("Inserindo 20 na posição 2...")
    lista.inserir(2, 20)
    lista.imprimir_lista()

    print("Inserindo 30 na posição 3...")
    lista.inserir(3, 30)
    lista.imprimir_lista()
    
    print("Inserindo 5 na posição 1...")
    lista.inserir(1, 5)
    lista.imprimir_lista()

    print("Inserindo 15 na posição 3...")
    lista.inserir(3, 15)
    lista.imprimir_lista()
    print()

    print("--- Verificando status pós-inserções ---")
    print(f"A lista está vazia? {lista.esta_vazia()}")
    print(f"Tamanho da lista: {lista.obter_tamanho()}")
    print()

    print("--- 4. Obter/modificar valor de um elemento ---")
    print(f"Valor na posição 1: {lista.obter_valor(1)}")
    print(f"Valor na posição 3: {lista.obter_valor(3)}")
    print(f"Valor na posição 5: {lista.obter_valor(5)}")
    
    print("Modificando valor na posição 3 para 99...")
    lista.modificar_valor(3, 99)
    print("Lista após modificação:")
    lista.imprimir_lista()
    print()

    print("--- 6. Retirar um elemento ---")
    print("Retirando elemento da posição 1...")
    valor_retirado = lista.retirar(1)
    print(f"Valor retirado: {valor_retirado}")
    lista.imprimir_lista()
    print(f"Novo tamanho da lista: {lista.obter_tamanho()}")
    
    print("\nRetirando elemento da última posição (4)...")
    valor_retirado = lista.retirar(4)
    print(f"Valor retirado: {valor_retirado}")
    lista.imprimir_lista()
    print(f"Novo tamanho da lista: {lista.obter_tamanho()}")

    print("\nRetirando elemento da posição 2...")
    valor_retirado = lista.retirar(2)
    print(f"Valor retirado: {valor_retirado}")
    lista.imprimir_lista()
    print(f"Novo tamanho da lista: {lista.obter_tamanho()}")
    print()

    print("--- 7. Imprimir os elementos da lista final ---")
    lista.imprimir_lista()