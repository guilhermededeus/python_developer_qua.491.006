import Curso
import Aluno

def main():
    # Intância as classes
    curso1 = Curso.Curso(nome_curso="Python")
    curso2 = Curso.Curso(nome_curso="Java")
    aluno1 = Aluno.Aluno(nome_aluno="Guilherme", matricula="1")
    aluno2 = Aluno.Aluno(nome_aluno="Matheus", matricula="2")
    aluno3 = Aluno.Aluno(nome_aluno="Pedro", matricula="3")
    aluno4 = Aluno.Aluno(nome_aluno="Maria", matricula="4")
    aluno5 = Aluno.Aluno(nome_aluno="Ana", matricula="5")
    aluno6 = Aluno.Aluno(nome_aluno="Julia", matricula="6")

    # Inscreve alunos no curso 1
    aluno1.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso1)
    aluno3.inscrever_curso(curso1)
    aluno4.inscrever_curso(curso1)

    # Inscreve alunos no curso 2
    aluno5.inscrever_curso(curso2)
    aluno6.inscrever_curso(curso2)


    print(f"Curso: {curso1.nome_curso}\nAlunos: {curso1.listar_alunos()}")


if __name__ == "__main__":
    main()