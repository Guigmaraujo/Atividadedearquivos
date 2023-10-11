def carregar_estudantes():
    estudantes = []
    with open('estudantes.txt', 'r') as arquivo:
        dados_estudante = {}
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                chave, valor = linha.split(': ')
                dados_estudante[chave] = valor
            else:
                estudantes.append(dados_estudante)
                dados_estudante = {}
    return estudantes

def contar(estudantes):
    contagem_cursos = {}
    for estudante in estudantes:
        curso = estudante['Curso do Estudante']
        if curso in contagem_cursos:
            contagem_cursos[curso] += 1
        else:
            contagem_cursos[curso] = 1
    return contagem_cursos

estudantes = carregar_estudantes()
contagem_cursos = contar(estudantes)

print("Contagem de Estudantes por Curso:")
for curso, quantidade in contagem_cursos.items():
    print(f"{curso}: {quantidade} estudante(s)")