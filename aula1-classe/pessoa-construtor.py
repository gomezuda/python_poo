class Pessoa:
    #Criando o método construtor
    def __init__(self, nome, hobby, endereco):
        #criando os atributos da classe utilizando o método construtor. Nesse caso presenciamos passar os parâmetros que serão usados como valores dos atributos.
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco

#Criando os métodos normais
def exibirDados(self):
    print(f"Olá {self.nome} seu hobby é {self.hobby} e seu endereço é {self.endereco}")

    #CRIANDO OS OBJETOS
    pessoal = Pessoa("Geraldo", "Corredor", "Rua 10 cohab")
    pessoal.exibirDados()# chamando o método da classe

    pessoa2 = Pessoa("Karla", "Artes Marciais", "Av 12 Renascença")
    print(pessoa2.nome)
