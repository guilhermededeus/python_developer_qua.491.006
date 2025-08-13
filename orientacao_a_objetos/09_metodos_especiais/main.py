import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="Guilherme", idade=20)
    print(usuario)
    print(f"Idade: {len(usuario)}")

    # Destruição do objeto
    del(usuario)

if __name__ == "__main__":
    main()