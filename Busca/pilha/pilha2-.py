from lib.stack import Stack

analisador = Stack()

expr = 'x + (9-((y*2)/3) +1)'

tem_erro = False
# Percorrer a espressao 
for pos in range(len(expr)):
    if expr[pos] == '(':
        analisador.push(pos)
    elif expr[pos] == ')':
        if analisador.is_empty:
            print(f'Erro de sintaxe na posição {pos}')
            tem_erro = True
        else:
            pos_abre = analisador.pop()
            print(f'Abre parentese da posicao {pos_abre} correspondente ao fecha parentese da posicao {pos}')


if not tem_erro:
    print ('Parenteses corretamente balanceados')

while not analisador.id_empty:
        pos_abre = analisador.pop()
        print(f'Erro : Abre parenteses da posicao {pos_abre} não tem o fecha parenteses correspondente')