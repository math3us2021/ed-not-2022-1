"""
ESTRUTURA DE DADOS DEQUE
Deque (pronúncia: dek-que) é uma estrutura de dados que permite adicionar e remover elementos no início e no fim da lista.

"""

class Deque:
    '''Metodo construtor'''
    def __init__(self):
        # inicia uma lista vazia
        self.__data = []  # lista de dados vazia

    # Metodo para inserção no inicio da fila
    def insert_front(self, val):
        self.__data.insert(0, val)



    # Metodo para inserção no final da fila
    def insert_back(self, val):
        self.__data.append(val)

    # Metodo para remoção no final da fila (deque)
    def remove_back(self):
        if self.is_empty:
            raise Exception('ERRO: impossível remover de uma fila vazia')
        # Remove o primeiro elemento da fila
        return self.__data.pop()


    # Metodo de consulta do inicio da fila
    def peek_front(self):
        if self.is_empty():
            raise Exception('ERRO: impossível consultar um deque vazio')
        else:
            return self.__data[-1]


    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__data[0]


    def __str__(self) -> str:
        return str(self.__data)