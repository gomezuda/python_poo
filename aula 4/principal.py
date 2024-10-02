funcionariol = Funcionario ("Gerente", 3000)
print("Seu cargo atual é: ", funcionario1.getCargo())

#Tentando mudar o valor do atributo
funcionariol.cargo = "Supervisor" #Acessando o atributo direto
funcionariol.setCargo ("Engenheiro") #Acessando o método para mudar o cargo
print("Seu cargo atual é: ", funcionario1.getCargo())

#Exibindo o salário
print("O seu salário atual é: ", funcionario1. salario)

funcionario1.salario = -100
print("O seu salário atual é: ", funcionariol.salario)