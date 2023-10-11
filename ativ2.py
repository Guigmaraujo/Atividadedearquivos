dados_lidos = {}

with open('estudantes.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        if linha.startswith('Nome'):
            nome = linha[len('Nome do Estudante: '):]
            estudante_atual = {'nome' : nome}

        elif linha.startswith('Idade'):
            idade = linha[len('Idade do Estudante: '):]
            estudante_atual['idade'] = idade
        
        elif linha.startswith('Curso'):
            curso = linha[len('Curso do Estudante: '):]
            estudante_atual['curso'] = curso
            dados_lidos[nome] = estudante_atual

for nome, info in dados_lidos.items():
    print(f"Nome: {nome}, Idade: {info['idade']}, Curso: {info['curso']}")
        
    