class Pessoa: 
    #Atributos - são as características da classe
    nome = "Fulano"
    idade = 25
    altura = 1.60 

    #Métodos - são os comportamentos da classe
    def falar (self,texto): #Self - parâmetro obrigatório do python que informa que o método pertence à própria classe que foi criada
        print(f"tenho algo para te falar : {texto}")

        #CRIANDO OBJETOS
        pessoal = Pessoa() #dessa forma estamos criando um objeto do tipo pessoa

        print(pessoa.nome, pessoal.idade)
        pessoal.falar("Bom dia, hoje é segunda-feira")