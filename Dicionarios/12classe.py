#Classe é uma estrutura que representa conjuntamente dados e algoritmos.Uma classe é como uma "forma de bolo",com a qual se pode criar diferentes "bolas"(objetos). variando os "ingredientes"(dados)e o "mode fazer" (algoritmo). Apesar dessa variação , os objetos criados a partir da 

class FormaGeometrica: 
    #Uma classe pode ter dentro de si, tanto dados quanto funções (esta representando os algoritmos)
    def __init__(self,base,altura,tipo):
        self.base = base
        self.altura = altura
        self.tipo = tipo

forma1 = FormaGeometrica(12,7, "R") #isso chama init
forma2 = FormaGeometrica(7.5,8.2, "T")

print(f"Forma 1 : {forma1.base}, altura: {forma1.altura}, tipo: {forma1.tipo}")
print(f"Forma 2 : {forma2}")
