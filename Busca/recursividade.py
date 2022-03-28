#o fatorial de im n inteiro > 1 pode ser definido recursivamente, como:
# n! = n *(n-1)!
# Já o fatorial de n=1 é definido como 1= 1!

#implementação ITERATIVA de um fatorial
from pickle import NONE
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


def fatorial_iter(n):
    resultado =1
    #range comeca em n e vai descendo ate 1

    for i in range(n, 1, -1):
        resultado *= i
    return resultado



#implementação Recursiva de um fatorial
def fatorial_rec(n):
    if n == 1 or n ==0:
        return 1 # condição de saida
    elif n>1:
        return n * fatorial_rec(n-1)
    else:
        return NONE

        ###########################################

# print(f"6! é igual a {fatorial_iter(6)}")
# print(f"31! é igual a {fatorial_iter(31)}")

print(f"6! é igual a {fatorial_rec(6)}")
print(f"31! é igual a {fatorial_rec(8)}")



##################################################