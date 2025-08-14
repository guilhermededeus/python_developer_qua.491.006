import Pessoa 
from dataclasses import dataclass

@dataclass
class PessoaFisica(Pessoa.Pessoa):
    nome: str
    cpf: str
    idade: int

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {len(self)}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"
    
    def __len__(self):
        return self.idade