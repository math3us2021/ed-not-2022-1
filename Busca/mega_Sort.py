# ALGORITMO DE ORDENACAO MERGE SORT

# No processo de ordenação, esse algoritmo "desmonta" o vetor inicial contendo N elementos,
# até obter N vetores de apenas um elemento cada um.
# Em seguida, usando a tecnica de mesclagem(merge), "Remonta o vetor, dessa vez, com os elementos já em ordem


# lista = [7,4,2,6,0,3,9,1,5,8]

# #Acha o meio da lista
# meio = len(lista) //2
# #////len é o comprimento dividido por dois

# metade1 = lista[0:meio]
# metade2 = lista[meio:]
# # : fatia a lista
# print(f"Meio: {meio}")
# print(f"lista: {lista}")
# print(f"Metade1 : {metade1}")
# print(f"Metade2: {metade2}")


def merge_sort(lista):
    # print(f"Lista recebida: {lista}")

    # Só continua se o comprimento da lista for maior que 1
    if len(lista) <= 1:
        return lista

# Encontra a possição do meio da lista
    meio = len(lista) // 2

    # Copia da primeira metade do vetor
    sublista_esquerda =lista[0:meio]
    sublista_direita =lista[meio:]
# Chamamos recursivamente a função para q ela continue repartindo cada uma das sublistas em metade

    sublista_esquerda = merge_sort(sublista_esquerda)
    sublista_direita = merge_sort(sublista_direita)

    #Aqui começa a junção das duas metades da lista, ordenadamente
    pos_esquerda = pos_direita = 0
    ordenada = [] #lista vazia

    #Compara os elementos da sublista entre si si e insere na lista ordenada o for menor
    while pos_esquerda < len(sublista_esquerda) and pos_direita < len(sublista_direita):
        # O elemento q se encontra na posicao da sublista esquerda é menor que o q se encontra na posicao da #sublista_direita

        if sublista_esquerda[pos_esquerda] < sublista_direita[pos_direita]:
            ordenada.append(sublista_esquerda[pos_esquerda])
            pos_esquerda +=1

        else:
            ordenada.append(sublista_direita[pos_direita])
            pos_direita +=1


    #verificar da sobra
    sobra=[]
    if pos_esquerda < pos_direita: sobra = sublista_esquerda[pos_esquerda:]
    else: sobra = sublista_direita[pos_direita:]

    #O resultado final é a concatenação da lista ordenada com sobra
    return ordenada + sobra



##################################################################

nums = [7,4,2,9,0,6,5,3,1,8]
resultado = merge_sort(nums)
print(resultado)
    # print(f"Esquerda : {sublista_esquerda}")
    # print(f"Direita : {sublista_direita}")
    # print(f"")
