import sys


# Requisito 12
def analyzer_menu():
    opcoes_de_menu = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )

    segunda_opcao = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a tag:",
        "4": "Digite a categoria:",
    }

    if opcoes_de_menu in ["5", "6", "7"]:
        print("")
    elif opcoes_de_menu in segunda_opcao:
        input(segunda_opcao[opcoes_de_menu])
    else:
        sys.stderr.write("Opção inválida\n")
