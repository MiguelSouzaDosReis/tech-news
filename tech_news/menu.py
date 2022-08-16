# # Requisito 12
import sys


def analyzer_menu():
    number = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.")
    obj = {
        "0": zero(),
        "1": one(),
        "2": two(),
        "3": tree(),
        "4": four(),
        "5": '5',
        "6": '6',
        "7": '7'
    }
    try:
        return obj[number]
    except Exception:
        return print("Opção inválida", file=sys.stderr)


def zero():
    return "Digite quantas notícias serão buscadas:"


def one():
    return "Digite o título:"


def two():
    return "Digite a data no formato aaaa-mm-dd:"


def tree():
    return "Digite a tag:"


def four():
    return "Digite a categoria:"
