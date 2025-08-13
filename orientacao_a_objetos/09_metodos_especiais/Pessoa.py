class Pessoa:
    # Construtor 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Olá, meu nome é {self.nome} e tenho {len(self)} anos."
    
    def __len__(self):
        return self.idade
    
    def __del__(self):
        return (f"Objeto {self.nome} destruido com sucesso.")