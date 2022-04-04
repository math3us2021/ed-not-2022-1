# ALGORITMO DE ORDENAÇÃO QUICK SORT

# Escolhe u dos elementos da lista para ser o pivô( na nossa implementação o ultimo elemento)
# na primeira passado, divide a lista, a partir da posição final da lista,em um sublista á esquerda
# conyendo apenas valores
from data.nomes_desord import nomes
# from time import time

passadas = comps = trocas = 0

def quick_sort(lista, ini=0, fim=None):
    # None = inexistente( se eu não passar posição, ele vai ser o ultimo da lista)
    if fim is None:fim = len(lista) -1
    global passadas, comps, trocas
    # Para q o algoritmo de ordenação trabalhe, é necesspario que haja, pelo menos, DOIS elementos
    # na faixa delimitada por ini e fim
    passadas += 1
    
    if fim <= ini:return

    
    # Inicialização das variaveis de controle
    pivot = fim
    div = ini - 1

    # Percorre a lista da posição ini ate a posicao fim -1
    for i in range(ini, fim):
        # compara os elementos das posições i e pivot
        comps += 1
        if lista[i] < lista[pivot]:

            div += 1  # Incrementa a posição do divisor se i e div não porem a mesma posição
            # os respectivos elementos trocam de posicao entre si
            if div != i:
                lista[i], lista[div] = lista[div], lista[i]
                trocas += 1
# Depois que o loop acaba, o divisor sofre um ultimo incremento
    div += 1

# Os elementos da posição de div e da posição de pivot trocam de lugar entre si se:
# 1) Os posições div e pivot forem diferentes entre si
# 2) lista(pivot) for menor que a lista(div)
    if div != pivot and lista[pivot] < lista[div]:
        lista[pivot], lista[div] = lista[div], lista[pivot]

    # Chamada recursiva a função para ordenar a sublista da posicao a esquerda
    quick_sort(lista, ini, div - 1)

    quick_sort(lista, div + 1, fim)

# nums = [7, 4, 2, 9, 0, 6, 8, 3, 1, 5]
quick_sort(nomes)
print(nomes)
print(f"Passadas:{passadas}, comparações {comps}, trocas: {trocas}")
