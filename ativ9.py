def adicionar_produto(compras, produto, preco):
    compras[produto] = preco

def atualizar_preco(compras, produto, novo_preco):
    if produto in compras:
        compras[produto] = novo_preco
        print(f"Preço do produto '{produto}' atualizado para {novo_preco:.2f} reais.")
    else:
        print(f"Produto '{produto}' não encontrado.")

def calcular_valor_total(compras):
    valor_total = sum(compras.values())
    return valor_total

def main():
    compras = {}

    while True:
        print("""
Menu:
[1] Adicionar Produto
[2] Atualizar Preço
[3] Calcular Valor Total
[4] Sair
        """)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: R$"))
            adicionar_produto(compras, produto, preco)
            print(f"Produto '{produto}' adicionado com sucesso.")
        elif escolha == '2':
            produto = input("Digite o nome do produto que deseja atualizar: ")
            novo_preco = float(input("Digite o novo preço: R$"))
            atualizar_preco(compras, produto, novo_preco)
        elif escolha == '3':
            valor_total = calcular_valor_total(compras)
            print(f"Valor total das compras: {valor_total:.2f} reais")
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()