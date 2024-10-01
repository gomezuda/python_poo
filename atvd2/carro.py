class Carro:
    #criando os atributos utilizando o método construtor
    def __init__(self, marca, modelo, ano, precoDiaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precoDiaria = precoDiaria

    def exibirDetalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Preço da Diária: R${self.precoDiaria:.2f}")

   # tive ajuda de Pablo!
    def calcularPrecoAluguel(self):
        Dias = int(input("Dias: "))
        Soma = Dias * self.precoDiaria
        print(f" Dias: {Dias * self.precoDiaria}") #processo pra mutiplicação