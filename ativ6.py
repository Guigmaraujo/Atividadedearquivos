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
                idade = int(linha[len('Idade do Estudante: '):])
            elif linha.startswith('Curso do Estudante: '):
                curso = linha[len('Curso do Estudante: '):]
                if nome_estudante and idade is not None and curso:
                    estudantes[nome_estudante] = {'Idade': idade, 'Curso': curso}
                    nome_estudante = None
                    idade = None
                    curso = None
    return estudantes

def calcular_idade_media(estudantes):
    idades = [dados['Idade'] for dados in estudantes.values()]
    if idades:
        return sum(idades) / len(idades)
    else:
        return 0

estudantes = carregar_estudantes()
idade_media = calcular_idade_media(estudantes)

print(f"A idade média dos estudantes é: {idade_media:.2f} anos")