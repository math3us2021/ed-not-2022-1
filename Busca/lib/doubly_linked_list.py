"""
    Classe que representa uma unidade de informação
    na lista duplamente encadeada
"""
from platform import node


class Node:

    """ Método construtor """

    def __init__(self, data):
        self.prev = None    # Ponteiro para o nodo anterior
        self.data = data    # Dado do usuário
        self.next = None    # Ponteiro para o nodo seguinte

##################################################################


"""
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos (nodos)
    não estão adjacentes fisicamente uns dos outros, mas ligados
    logicamente por meio de ponteiros que indicam o anterior e
    o próximo nodo da sequência. Não tem restrição de acesso -
    inserções, exclusões e consultas podem ser realizados em
    qualquer posição da lista.
"""


class DoublyLinkedList:

    """ Método construtor """

    def __init__(self):
        self.__head = None  # Aponta para o primeiro nodo da lista
        self.__tail = None  # Aponta para o último nodo da lista
        self.__count = 0    # Mantém o número de nodos da lista


@property
def count(self):
    return self.__count


@property
def is_empty(self):
    return self.__count == 0


#'''Metodo que insere um modo na posição especifica'''


def insert(self, pos, val):
    # Criamos um modo q contem a informaçãodo usuario e tambei um ponteiro para o nodo anterior
    inserted = Node(val)
    # Se a lista estiver vazia então o modo inserido será o primeiro e o ultimo
    if self.is_empty():
        self.__head = inserted
        self.__tail = inserted


#'''2° Caso - Inserção no inicio'''
    elif pos == 0:
        inserted.next = self.__head
        self.__head.prev = inserted
        self.__head = inserted

        '''3° Caso - Inserção no final'''
    elif pos == self.count:
        self.__tail.next = inserted
        inserted.prev = self.__tail
        self.__tail = inserted

#''' 4° Caso - Inserção no meio'''
    else:
        node_pos = self.__find_node(pos)
        # Inserimos o nodo na posição especificada
        before = node_pos.prev

        before.next = inserted
        inserted.prev = before
        inserted.next = node_pos
        node_pos.prev = inserted

    # incrementando a contadem de itens da lista
    self.__count += 1


#"""'''Função privada para encontrar um no na posicao especifica'''"""

def __find_node(self, pos):
    if pos == 0:
        return self.__head


    elif pos == self.count -1:
        return self.__tail

    else:
        if pos <= self.count //2:
            node = self.__head
            for i in range(1,pos + 1): 
                node = node.next
    
        else:
            node = self.__tail
            for i in range(self.count - 2, pos -1, -1):
                node = node.prev

        return node
                