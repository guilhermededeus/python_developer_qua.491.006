import Pessoa 
from dataclasses import dataclass

@dataclass
class PessoaJuridica(Pessoa.Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str

    def __str__(self):
        return f"Razão social: {self.razao_social}\nNome fantasia: {self.nome_fantasia}\nCNPJ: {self.cnpj}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"