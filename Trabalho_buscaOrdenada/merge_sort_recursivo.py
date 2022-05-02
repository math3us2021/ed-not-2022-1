from time import time
import tracemalloc
from trabalho.emp100mil import empresas

def merge_sort(empresas):
    """
        Função que implementa o algoritmo Merge Sort de forma ITERATIVA
    """

    # Inicia com o menor tamanho de partição de 2^0 = 1
    tam_part = 1
    n = len(empresas)
    
    # O tamanho da sublista cresce em potências de 2
    while (tam_part < n):
        # Inicia sempre pela esquerda
        esq = 0
        while (esq < n):
            dir = min(esq + (tam_part * 2 - 1), n - 1)
            meio = (esq + dir)//2

            # print(f"esq: {esq}, dir: {dir}, meio: {meio}")

            # A mescla final deve considerar sublistas
            # não mescladas se o tamannho da lista original
            # não for potência de 2
            if (tam_part > n//2):
                meio = dir  - (n % tam_part)
            
            tam_esq = meio - esq + 1
            tam_dir = dir - meio
            empresas_esq = [0] * tam_esq   # Vetor auxiliar
            empresas_dir = [0] * tam_dir   # Vetor auxiliar
            for pos_esq in range(0, tam_esq):
                empresas_esq[pos_esq] = empresas[esq + pos_esq]
            for pos_esq in range(0, tam_dir):
                empresas_dir[pos_esq] = empresas[meio + pos_esq + 1]

            pos_esq, pos_dir, i = 0, 0, esq
            while pos_esq < tam_esq and pos_dir < tam_dir:
                if empresas_esq[pos_esq] > empresas_dir[pos_dir]:
                    empresas[i] = empresas_dir[pos_dir]
                    pos_dir += 1
                else:
                    empresas[i] = empresas_esq[pos_esq]
                    pos_esq += 1
                i += 1

            while pos_esq < tam_esq:
                empresas[i] = empresas_esq[pos_esq]
                pos_esq += 1
                i += 1

            while pos_dir < tam_dir:
                empresas[i] = empresas_dir[pos_dir]
                pos_dir += 1
                i += 1

            esq += tam_part * 2
        # Incrementa a sublista em potências de 2
        tam_part *= 2
    return empresas

############################################################

# nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

empresas_ord = merge_sort(empresas)

print(empresas_ord)

hora_ini = time()
tracemalloc.start()
merge_sort(empresas)
new_atual, mem_pico = tracemalloc.get_traced_memory()
hora_fim = time()


print(f"Tempo gasto para ordenar: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: {mem_pico /1024/1024}MB")