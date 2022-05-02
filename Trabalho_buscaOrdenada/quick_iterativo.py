


from time import time
from trabalho.emp100mil import empresas
import tracemalloc


passadas = comps = trocas = 0




def quick_sort(lista, ini = 0, fim = None):
    """
        Função que implementa o algoritmo Quick Sort de forma ITERATIVA
    """

    if fim is None: fim = len(lista) - 1
    global passadas, comps, trocas
   
    # Cria uma lista auxiliar
    tamanho = fim - ini + 1
    aux = [None] * tamanho
    
    # Inicializa a posição da lista auxiliar
    pos = -1
    
    # Coloca os valores iniciais de ini e fim na lista auxiliar
    pos = pos + 1
    aux[pos] = ini
    pos = pos + 1
    aux[pos] = fim
    
    # Continua retirando valores da lista auxiliar enquanto
    # ela não estiver vazia
    while pos >= 0:

        # print(aux)
  
        # Retira fim e início
        fim = aux[pos]
        pos = pos - 1
        ini = aux[pos]
        pos = pos - 1
        passadas += 1
        # Coloca o pivô em sua posição correta na lista ordenada
        i = ini - 1
        x = lista[fim]
    
        for j in range(ini , fim):
            if lista[j] <= x:
                # Incrementa a posição do menor elemento
                i = i + 1
                comps += 1
                lista[i], lista[j] = lista[j], lista[i]
                
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        
        pivot = i + 1
  
        # Se há elementos à esquerda do pivô, coloca-os
        # no lado esquerdo da lista auxiliar
        if pivot - 1 > ini:
            trocas += 1
            pos = pos + 1
            aux[pos] = ini
            pos = pos + 1
            aux[pos] = pivot - 1
  
        # Se há elementos à direita do pivô, coloca-os
        # no lado direito da lista auxiliar
        if pivot + 1 < fim:
            pos = pos + 1
            aux[pos] = pivot + 1
            pos = pos + 1
            aux[pos] = fim

########################################################################

# nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66] 

# quick_sort(nums)

# print(nums)  

hora_ini = time()
tracemalloc.start()
quick_sort(empresas)
new_atual, mem_pico = tracemalloc.get_traced_memory()
hora_fim = time()


print(empresas)
print(f"Tempo gasto para ordenar: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: {mem_pico /1024/1024}MB")
print(f"Passadas:{passadas}, comparações {comps}, trocas: {trocas}")
