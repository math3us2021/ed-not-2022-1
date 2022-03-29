# Um dicionário é uma estrutura de dados fornecuda pela linguagem Python, capaz de armazenar multiplos valores em uma unica variável, por meio de pares de chave-valor

pessoa={
    #"nome" é a chave
    #Gervasio Gomes Garcia é o valor
    "nome": "Gevásio Gomes Garcia",
    "sexo": "M",
    "Idade":69,
    "peso":76,
    "altura":1.77
}

print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['Idade']}")

#Calculando o indice de massa corporea
imc = pessoa ["peso"]/pessoa["altura"]**2

print(f"IMC: {imc}")

#FORMAS GEOMETRICAS

forma1={
    "base":7.5,
    "altura":12,
    "tipo":"R" # Retangulo
}

forma2={
    "base":6,
    "altura":2.5,
    "tipo":"T" # triangulo
}
forma3={
    "base":5,
    "altura":3,
    "tipo":"E" # Elipse
}

forma4={
    "base":10,
    "altura":5,
    "tipo":"R" # Retangulo
}
# Forma geometrica completamente anomala
forma5={
    "base":"Batata",
    "altura": "jabuticaba",
    "tipo":"T"
}

# Inserindo as formas em uma lista para percorrer com for

lista_formas = [forma1,forma2,forma3,forma4,forma5]

#Funcao que calcula o area de uma forma de acordo com a base, a altura e o tipo

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R": # Retangulo
        return forma["base"]*forma["altura"]
    elif forma["tipo"] == "T": # Triangulo
        return (forma["base"]*forma["altura"])/2
    elif forma["tipo"] == "E":# Elipse
        return (forma["base"]/2)*(forma["altura"]/2)*pi
    else:
        return Exception("Forma geometrica nao conhecida")

# Calculando a area de todas as formas da lista

for i in range(0,len(lista_formas)):
    print("-" * 30)
    print(lista_formas[i])
    print(f"Calculando Area da forma {i+1}:")
    print(f"Tipo: {lista_formas[i]['tipo']}; base:{lista_formas[i]['base']}; altura: {lista_formas[i]['altura']}; área: {calcular_area(lista_formas[i])}" )