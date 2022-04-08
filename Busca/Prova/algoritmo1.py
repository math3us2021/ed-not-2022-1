"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""
# 1)  ALGORITMO DE ORDENAÇÃO MERGE SORT merge sort.
# 2) Comentários das variavéis no código
# 3) O erro esta na ausencia do ultimo return, na ultima linha do codigo. Foi incluido no código.


#  COMPARATIVO UTILIZADO PARA FACILITAR MEU ENTENDIMENTO
# a = merge sort (funcao)
# b = lista
# c = meio
# d = sublista_esquerda
# e = sublista_direita
# f = pos_esquerda
# g = pos_direita
# h = ordenada
# i = sobra


def a(b):  # Abrindo a função
    if len(b) <= 1: return b  # Se o tamanho da lista for menor ou igual a 1, retorna a lista
    c = len(b) // 2 # Encontra a posição do meio da lista

    d = b[:c] # Cópia da primeira metade do vetor.Encontra a sublista da esquerda, a partir do inicio da lista até o meio
    e = b[c:] # Cópia da segunda metade do vetor. Encontra a sublista da direita, a partir do meio da lista até o fim
    d = a(d) # Chama a função recursivamente para a sublista da esquerda
    e = a(e) # Chama a função recursivamente para a sublista da direita

    # AQUI COMEÇA A JUNÇÃO DAS DUAS METADES DA LISTA, ORDENADAMENTE
    f = g = 0 # Posição da esquerda e direita
    h = [] 
    while f < len(d) and g < len(e): # Enquanto o f for menor que o tamanho da primeira metade e o g for menor que o tamanho da segunda metade
        if d[f] < e[g]: # Se o elemento da primeira metade for menor que o elemento da segunda metade
            h.append(d[f]) # Adiciona o elemento da primeira metade na lista ordenada
            f += 1
        else:
            h.append(e[g]) # Adiciona o elemento da segunda metade na lista ordenada
            g += 1
    i = [] # Lista vazia
    if f < g: i = d[f:] # Se o f for menor que o g, a sobra da primeira metade é inserida na lista
    else: i = e[g:] # Se o contrário, a sobra da segunda metade é inserida na lista
    return h + i # Retorna a junção das duas metades ordenadas