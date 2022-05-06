
class Queue:
    '''Metodo construtor'''
    def __init__(self):
        # inicia uma lista vazia
        self.__data = []

    ''' Método para inserir um elemento no final da fila '''
    def enqueue(self, val):
        self.__data.append(val)

    ''' Método para retirar um elemento do inicio da fila '''
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.__data.pop(0)
    
    ''' Método para verificar se a fila está vazia '''
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__data[0]

    def __str__(self) -> str:
        return str(self.__data)

    