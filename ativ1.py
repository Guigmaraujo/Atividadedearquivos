estudantes = []

while True:

    nomeestudante = input("Digite o nome: ")
    idadeestudante = input("Digite a idade: ")
    cursoestudante = input("Digite o curso: ")

    estudantes.append({
        "nome" : nomeestudante,
        "idade" : idadeestudante,
        "curso" : cursoestudante,
    })

    print("""
[ 1 ] Continuar inserindo
[ 2 ] Salvar
          """)
    
    opcao = int(input("Digite a opção: "))

    if opcao == 2:
        break
    else:
        continue

with open('estudantes.txt', 'a') as arquivo:
    for estudante in estudantes:
        arquivo.write(f"Nome do Estudante: {estudante['nome']}\n")
        arquivo.write(f"Idade do Estudante: {estudante['idade']}\n")
        arquivo.write(f"Curso do Estudante: {estudante['curso']}\n")
        arquivo.write(f"\n")