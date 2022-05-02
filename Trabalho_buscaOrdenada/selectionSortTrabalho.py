# ALGORITMO DE ORDENAÇÃO SELECTION SORT
#
# Isola (seleciona) o primeiro elemento da lista e, em seguida,
# encontra o menor valor no restante da lista. Se o valor encontrado
# for menor que o valor selecionado, efetua a troca.
# Em seguida, isola o segundo número da lista, buscando pelo menor
# valor das posições subsequentes. Faz a troca entre os dois valores,
# se necessário. Continua o processo, até isolar o penúltimo elemento
# da lista.

from trabalho.emp100mil import empresas
# from data.nomes_desord import nomes
from time import time
import tracemalloc
passadas = comps = trocas = 0

def selection_sort(lista):

    global passadas, comps, trocas
    passadas = comps = trocas = 0

    # Subfunção que encontra o menor valor na sublista
    # delimitada por pos_ini e pos_fim
    def encontrar_pos_menor(pos_ini, pos_fim):
        global comps
        pos_res = pos_ini
        # Loop da segunda até a última posição
        for pos in range(pos_ini + 1, pos_fim + 1):
            comps += 1
            if lista[pos] < lista[pos_res]:
                pos_res = pos
        return pos_res

    # Loop que vai da primeira até a PENÚLTIMA posição
    for pos_sel in range(len(lista) - 1):
        passadas += 1
        # Encontra o menor valor na faixa entre o número seguinte
        # a pos_sel e o fim da lista
        pos_menor = encontrar_pos_menor(pos_sel + 1, len(lista) - 1)

        # Compara se o menor valor encontrado é ainda menor que
        # o valor da posição selecionada
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            # Efetua a troca
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

###################################################################

#nums = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]
#nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# nums = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# selection_sort(nomes)
# print(nomes)     
# print(f"passadas: {passadas}, comparações: {comps}, trocas: {trocas}")   

hora_ini = time()
tracemalloc.start()
selection_sort(empresas)
new_atual, mem_pico = tracemalloc.get_traced_memory()
hora_fim = time()

print(empresas)
print(f"Tempo gasto para ordenar: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: {mem_pico /1024/1024}MB")
print(f"passadas: {passadas}, comparações: {comps}, trocas: {trocas}")