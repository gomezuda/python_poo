class Funcionario:
    #Criando o método construtor
    def __init__(self, nome, cargo, salario): #chamado quando você cria uma nova instância da classe
        #criando os atributos da classe utilizando o método construtor.
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibirdados(self): 
        print(f"Funcionário: {self.nome}, Cargo: {self.cargo}, Salário: R$ {self.salario:.2f}")
    def verificarsalario(self): 
        if self.salario <= 2000: 
            print("direito a bônus")
        else: 
            print("sem direito a bônus")
