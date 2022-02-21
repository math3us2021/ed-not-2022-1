###################################################
# BUSCA SEQUENCIAL
#
# Procura por um valor na lista, partindo do primeiro
# elemento até o último. Retorna:
# a) a posição do elemento, caso ele exista; ou
# b) -1, se o elemento não existir

nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]

"""
    Função que implementa a busca sequencial
    Procura por val dentro de lista
"""
def busca_sequencial(val, lista):
    for pos in range(len(lista)):
        # Se encontra coincidência, retorna a posição
        if lista[pos] == val: return pos
    return -1   # Nada encontrado

print(f"Posição de 27: {busca_sequencial(27, nums)}")
print(f"Posição de 40: {busca_sequencial(40, nums)}")
    