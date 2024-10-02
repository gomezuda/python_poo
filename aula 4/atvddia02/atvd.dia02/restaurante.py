class Servico:
    def __init__(self):
        self.__pedido = 0  #Armazena o número de pedidos

    def novoPedido(self):
        self.__pedido += 1  #Aumenta o contador de pedidos em 1 cada vez que um novo pedido é registrado.
    def cancelarPedido(self):
        if self.__pedido > 0:
            self.__pedido -= 1  # diminiu o número de pedidos
        else:
            print("Nenhum pedido pra cancelar.")

    def exibirPedido(self):
        return self.__pedido  #Retorna o número de pedidos
