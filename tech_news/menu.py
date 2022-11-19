import sys
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)


def func_0():
    value = input("Digite quantas notícias serão buscadas: ")
    get_tech_news(value)


def func_1():
    value = input("Digite o título: ")
    print(search_by_title(value))


def func_2():
    value = input("Digite a data no formato aaaa-mm-dd: ")
    print(search_by_date(value))


def func_3():
    value = input("Digite a tag: ")
    print(search_by_tag(value))


def func_4():
    value = input("Digite a categoria: ")
    print(search_by_category(value))


def func_5():
    print(top_5_news())


def func_6():
    print(top_5_categories())


def func_7():
    print("Encerrando script\n")


def interface_menu(opcao: str):
    funcoes = [
        func_0,
        func_1,
        func_2,
        func_3,
        func_4,
        func_5,
        func_6,
        func_7,
    ]
    try:
        funcao = funcoes[int(opcao)]
    except (KeyError, ValueError, IndexError):
        raise ValueError("Opção inválida")
    return funcao()


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
        " 7 - Sair.\n"
    )

    try:
        interface_menu(opcoes_de_menu)
    except SystemExit:
        raise
    except Exception as exc:
        print(exc, file=sys.stderr)
