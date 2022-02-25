def busca_binaria(lista, val):
    ini = 0 #POsicao inicial da lista
    fim = len(lista) -1 # posicao final da lista

    while ini <= fim: 
        meio = (ini + fim) // 2  # "//" é para divisao inteira, meio da lista
        # 1° caso : o valor na posicao do meio da lista corresponde ao valor buscado; 
        #ENCONTRAMOS e retornamos a posicao encontrada (meio)

        if val == lista(meio):
            return meio
        #2°caso - o valor de busca é maior que o valor no meio da lista
        elif val > lista(meio):
            ini = meio +1

        #3° caso - O valor de busca é menor que o valor no meio da busca da lista
        else:
            fim = meio -1
    