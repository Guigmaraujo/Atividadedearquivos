def carregar_estudantes():
    estudantes = {}
    with open('estudantes.txt', 'r') as arquivo:
        nome_estudante = None
        idade = None
        curso = None
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith('Nome do Estudante: '):
                nome_estudante = linha[len('Nome do Estudante: '):]
            elif linha.startswith('Idade do Estudante: '):
                idade = linha[len('Idade do Estudante: '):]
            elif linha.startswith('Curso do Estudante: '):
                curso = linha[len('Curso do Estudante: '):]
                if nome_estudante and idade and curso:
                    estudantes[nome_estudante] = {'Idade': idade, 'Curso': curso}
                    nome_estudante = None
                    idade = None
                    curso = None
    return estudantes

def exibir_informacoes(estudante):
    print("Informações do Estudante:")
    print(f"Nome: {estudante}")
    print(f"Idade: {estudantes[estudante]['Idade']}")
    print(f"Curso: {estudantes[estudante]['Curso']}")

nome_pesquisa = input("Digite o nome do estudante que deseja pesquisar: ")
estudantes = carregar_estudantes()

if nome_pesquisa in estudantes:
    exibir_informacoes(nome_pesquisa)
else:
    print("Estudante não encontrado.")