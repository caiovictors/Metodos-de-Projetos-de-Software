class Pessoa:
    def __init__(self, nome, idade):   	               #método - comportamento
        self.nome = nome			                   #atributo - estado
        self.idade = idade			                   #atributo - estado
        
    def andar(self, passos):                           #método - comportamento
        self.passos = passos                           
        print(self.nome, 'deu', self.passos, 'passos.')


def main():
    pessoa_1 = Pessoa('Caio', 21)
    Pessoa.andar(pessoa_1, 15)
main()