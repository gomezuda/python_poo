class Funcionario:
#Iremos ultilizar uma forma única do python para acessar e atribuir privados
    #Criando o 'get' do salário
    @property #criar um get 'mais bonito'
    def salario(self):
        return self. salario
    
    @salario.setter #criar um set para o salário 'mais bonito'
    def salario(self, valor):
        if valor <= 0:
            print("Informe um valor positivo")
        else:
            self.__salario = valor