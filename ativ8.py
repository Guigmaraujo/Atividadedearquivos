import os
from time import sleep

def carregar_contatos():
    contatos = {}
    if os.path.exists('contatos.txt'):
        with open('contatos.txt', 'r') as arquivo:
            for linha in arquivo:
                nome, telefone = linha.strip().split(',')
                contatos[nome] = telefone
    return contatos

def salvar_contatos(contatos):
    with open('contatos.txt', 'w') as arquivo:
        for nome, telefone in contatos.items():
            arquivo.write(f'{nome},{telefone}\n')

def adicionar_contato(contatos, nome, telefone):
    contatos[nome] = telefone

def visualizar_contatos(contatos):
    if not contatos:
        print("A agenda de contatos está vazia.")
    else:
        print("Contatos:")
        for nome, telefone in contatos.items():
            print(f"Nome: {nome}, Telefone: {telefone}")

def atualizar_contato(contatos, nome, novo_telefone):
    if nome in contatos:
        contatos[nome] = novo_telefone
        print(f"Contato '{nome}' atualizado com sucesso.")
    else:
        print(f"Contato '{nome}' não encontrado.")

def excluir_contato(contatos, nome):
    if nome in contatos:
        del contatos[nome]
        print(f"Contato '{nome}' excluído com sucesso.")
    else:
        print(f"Contato '{nome}' não encontrado.")

def main():
    contatos = carregar_contatos()

    while True:
        print("""
        Menu:
        [1] Adicionar Contato
        [2] Visualizar Contatos
        [3] Atualizar Contato
        [4] Excluir Contato
        [5] Sair
        """)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(contatos, nome, telefone)
            salvar_contatos(contatos)
        elif escolha == '2':
            visualizar_contatos(contatos)
        elif escolha == '3':
            nome = input("Digite o nome do contato que deseja atualizar: ")
            novo_telefone = input("Digite o novo telefone: ")
            atualizar_contato(contatos, nome, novo_telefone)
            salvar_contatos(contatos)
        elif escolha == '4':
            nome = input("Digite o nome do contato que deseja excluir: ")
            excluir_contato(contatos, nome)
            salvar_contatos(contatos)
        elif escolha == '5':
            print('Saindo.')
            sleep(1)
            print('Saindo..')
            sleep(1)
            print('Saindo...')
            sleep(1)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()