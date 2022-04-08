"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""
# 1) BUSCA SEQUENCIAL
# 2 ) Comentário das variavéis no código
# 3) O erro é no for, onde no lugar do c, é incluso o pos. Foi corrigido tambeém no if.

# b = lista
# c = valor
# pos = posição na lista
def a(b, c): # Abrindo a função
    for pos in range(len(b)): # Para cada elemento da lista
        if b[pos] == c: return pos # Se encontra coincidência, retorna a posição. Se o elemento for igual a sua posição na lista, retorna a posição
    return -1 # Se não for encontrado, retorna -1

   