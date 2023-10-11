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

nome = input("Digite o nome do estudante: ")
estudantes = carregar_estudantes()

if nome in estudantes:
    print("Estudante encontrado!")
    print("""
    [ 1 ] Idade
    [ 2 ] Curso
    [ 3 ] Sair
    """)
    opcao = input("Digite o que deseja mudar: ")
    if opcao == '1':
        nova_idade = input("Digite a nova idade: ")
        estudantes[nome]['Idade'] = nova_idade
        salvar_estudantes(estudantes)
        print("Idade atualizada com sucesso.")
    elif opcao == '2':
        novo_curso = input("Digite o novo curso: ")
        estudantes[nome]['Curso'] = novo_curso
        salvar_estudantes(estudantes)
        print("Curso atualizado com sucesso.")
    else:
        print("Saindo.")
else:
    print("Estudante não encontrado!")