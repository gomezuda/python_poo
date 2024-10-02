from contaBancaria import Conta

minhaConta = Conta(123,"Ermenegildo Sousa",1000,500)

minhaConta.detalhes()

minhaConta.saldo = 20000
minhaConta.detalhes

#Criando os demais métodos
def detalhes(self):
    print(f"O limite atual é {minhaConta.getLimite()}")

minhaConta.setLimite(259)#alterando o valor do limite

minhaConta.__limite = 2000
print(f"O limtie atual é {minhaConta.getLimite()}")
