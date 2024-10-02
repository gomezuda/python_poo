from restaurante import Servico
servico = Servico()

print("Teste do sistema de pedidos:")

servico.novoPedido()
servico.novoPedido()
print(f"Número de pedidos: {servico.exibirPedido()}")

servico.cancelarPedido()
print(f"Número de pedidos: {servico.exibirPedido()}")

servico.cancelarPedido()
print(f"Número de pedidos após outro cancelamento: {servico.exibirPedido()}")

servico.cancelarPedido()