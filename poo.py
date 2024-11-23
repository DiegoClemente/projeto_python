class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e minha idade é {self.idade}"

pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)
