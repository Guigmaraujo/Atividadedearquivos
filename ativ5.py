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

def salvar_estudantes(estudantes):
    with open('estudantes.txt', 'w') as arquivo:
        for nome, dados in estudantes.items():
            arquivo.write(f'Nome do Estudante: {nome}\n')
            arquivo.write(f'Idade do Estudante: {dados["Idade"]}\n')
            arquivo.write(f'Curso do Estudante: {dados["Curso"]}\n')
            arquivo.write('\n')

def remover_estudante(estudantes, nome_estudante):
    if nome_estudante in estudantes:
        del estudantes[nome_estudante]
        print(f"Estudante '{nome_estudante}' removido com sucesso.")
    else:
        print("Estudante não encontrado.")

estudantes = carregar_estudantes()
nome_remover = input("Digite o nome do estudante que deseja remover: ")

remover_estudante(estudantes, nome_remover)
salvar_estudantes(estudantes)