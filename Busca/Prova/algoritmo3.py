"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""
#1) # ALGORITMO DE ORDENAÇÃO SELECTION SORT
#2 ) Comentário das variavéis no código
#3) O erro esta no return g, sendo o correto return f .

# b = lista
# c = pos_menor
# d = pos_ini
# e = pos_fim
# f = pos_res 
# g = pos 
# h = pos_sel
# i = pos_menor
def a(b): # Abrindo a função
    def c(d, e): # Abrindo a função , d = pos_ini, e = pos_fim
        f = d # Posição inicial , f = pos_ini, d = pos_ini
        for g in range(d + 1, e + 1): # Para cada elemento da lista, sendo posição inicial  é acrescentado + 1 para conseguir realizar a comparação
            if b[g] < b[f]: # Se o elemento for menor que o elemento da posição inicial
                f = g # Posição inicial recebe a posição do elemento menor
        return g  #O erro estava aqui, pois retorna um f, f = pos_res.
    for h in range(len(b) - 1): 
        i = c(h + 1, len(b) - 1)
         # Compara se o menor valor encontrado é ainda menor que
        # o valor da posição selecionada
        if b[i] < b[h]: 
            b[i], b[h] = b[h], b[i] # Se for, troca os valores