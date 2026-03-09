# ============================================
#       LISTA DE COMPRAS SIMPLES
#   Bem-vindo ao seu gerenciador de compras!
# ============================================

lista_compras = []
proximo_id = 1

UNIDADES = {
    "1": "Quilograma",
    "2": "Grama",
    "3": "Litro",
    "4": "Mililitro",
    "5": "Unidade",
    "6": "Metro",
    "7": "Centímetro"
}


def exibir_cabecalho():
    print("\n" + "=" * 50)
    print("       LISTA DE COMPRAS SIMPLES")
    print("  Bem-vindo ao seu gerenciador de compras!")
    print("=" * 50)


def exibir_lista():
    if not lista_compras:
        print("\n[ Sua lista de compras está vazia. ]\n")
    else:
        print("\n📋 PRODUTOS NA LISTA:")
        print("-" * 60)
        print(f"{'ID':<5} {'Nome':<20} {'Qtd':<8} {'Unidade':<15} {'Descrição'}")
        print("-" * 60)
        for produto in lista_compras:
            print(
                f"{produto['id']:<5} "
                f"{produto['nome']:<20} "
                f"{produto['quantidade']:<8} "
                f"{produto['unidade']:<15} "
                f"{produto['descricao']}"
            )
        print("-" * 60)
        print(f"Total de produtos: {len(lista_compras)}\n")


def exibir_menu():
    print("MENU DE OPÇÕES:")
    print("  1. Adicionar produto")
    print("  2. Remover produto")
    print("  3. Pesquisar produtos")
    print("  4. Sair do programa")
    print()


def adicionar_produto():
    global proximo_id
    print("\n--- ADICIONAR PRODUTO ---")

    nome = input("Nome do produto: ").strip()
    if not nome:
        print("❌ Erro: O nome do produto não pode estar vazio.")
        return

    print("\nUnidades de medida disponíveis:")
    for chave, valor in UNIDADES.items():
        print(f"  {chave}. {valor}")

    opcao_unidade = input("Escolha a unidade de medida (1-7): ").strip()
    if opcao_unidade not in UNIDADES:
        print("❌ Erro: Opção de unidade inválida.")
        return
    unidade = UNIDADES[opcao_unidade]

    quantidade_str = input("Quantidade: ").strip()
    try:
        quantidade = float(quantidade_str)
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        print("❌ Erro: Quantidade inválida. Insira um número positivo.")
        return

    descricao = input("Descrição (opcional): ").strip()
    if not descricao:
        descricao = "—"

    produto = {
        "id": proximo_id,
        "nome": nome,
        "unidade": unidade,
        "quantidade": quantidade,
        "descricao": descricao
    }

    lista_compras.append(produto)
    proximo_id += 1
    print(f"\n✅ Produto '{nome}' adicionado com sucesso! (ID: {produto['id']})")


def remover_produto():
    print("\n--- REMOVER PRODUTO ---")

    if not lista_compras:
        print("⚠️  A lista está vazia. Nenhum produto para remover.")
        return

    id_str = input("Digite o ID do produto que deseja remover: ").strip()
    try:
        id_busca = int(id_str)
    except ValueError:
        print("❌ Erro: ID inválido. Insira um número inteiro.")
        return

    for produto in lista_compras:
        if produto["id"] == id_busca:
            lista_compras.remove(produto)
            print(f"\n✅ Produto '{produto['nome']}' (ID: {id_busca}) removido com sucesso!")
            return

    print(f"❌ Erro: Nenhum produto encontrado com o ID {id_busca}.")


def pesquisar_produtos():
    print("\n--- PESQUISAR PRODUTOS ---")

    if not lista_compras:
        print("⚠️  A lista está vazia. Nenhum produto para pesquisar.")
        return

    termo = input("Digite o nome ou parte do nome do produto: ").strip().lower()
    if not termo:
        print("❌ Erro: O termo de pesquisa não pode estar vazio.")
        return

    resultados = [p for p in lista_compras if termo in p["nome"].lower()]

    if not resultados:
        print(f"\n🔍 Nenhum produto encontrado com o termo '{termo}'.")
    else:
        print(f"\n🔍 {len(resultados)} produto(s) encontrado(s) para '{termo}':")
        print("-" * 60)
        print(f"{'ID':<5} {'Nome':<20} {'Qtd':<8} {'Unidade':<15} {'Descrição'}")
        print("-" * 60)
        for produto in resultados:
            print(
                f"{produto['id']:<5} "
                f"{produto['nome']:<20} "
                f"{produto['quantidade']:<8} "
                f"{produto['unidade']:<15} "
                f"{produto['descricao']}"
            )
        print("-" * 60)


def main():
    exibir_cabecalho()

    while True:
        exibir_lista()
        exibir_menu()

        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            pesquisar_produtos()
        elif opcao == "4":
            print("\n👋 Encerrando o programa. Até logo!\n")
            break
        else:
            print("❌ Opção inválida. Por favor, escolha entre 1 e 4.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()