###################################################
# BUSCA SEQUENCIAL
#
# Procura por um valor na lista, partindo do primeiro
# elemento até o último. Retorna:
# a) a posição do elemento, caso ele exista; ou
# b) -1, se o elemento não existir

nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
# from data.primos import primos
# from data.lista_nomes import nomes
# from time import time
"""
    Função que implementa a busca sequencial
    Procura por val dentro de lista
"""
def busca_sequencial(val, lista):
    for pos in range(len(lista)):
        # Se encontra coincidência, retorna a posição
        if lista[pos] == val: return pos
    return -1   # Nada encontrado

# hora_ini = time()
# print(f"Posição de 1487: {busca_sequencial(27, primos)}")
# hora_fim = time
# print(f"Posição de 1487: {(hora_fim - hora_ini)*1000}")
    
# hora_int = time()
# print(f"Posição de 7603: {busca_sequencial(7603, primos)}")
# hora_fim = time
# print(f"Posição de 7603: {(hora_fim - hora_ini)*1000}")

# hora_int = time()
# print(f"Posição de 8008: {busca_sequencial(8008, primos)}")
# hora_fim = time
# print(f"Posição de 8008: {(hora_fim - hora_ini)*1000}")


hora_ini = time()
print(f"Posicao do nome 'orkutilson' :{busca_sequencial('ORKUTILSON', nomes)}")
hora_fim = time ()
print(f"Tempo gasto para buscar ORKUTILSON:{(hora_fim - hora_ini) *1000}ms")