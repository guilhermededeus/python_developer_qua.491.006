# Importa o dataclass
from dataclasses import dataclass

# Classe Pessoa
@dataclass
class Pessoa:
    # Atributos
    nome: str
    email: str
    cpf: str
    idade: int
    altura: float

    def __str__(self):
        return f"Nome: {self.nome}\nEmail: {self.email}\nCPF: {self.cpf}\nIdade: {self.idade}\nAltura: {self.altura}"
    
    def __len__(self):
        return self.idade