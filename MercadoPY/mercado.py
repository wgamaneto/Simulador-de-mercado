from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('Bem-Vindo(a)')
    print('Meu Shopping')

    print('Selecione uma opcao abaixo: ')
    print('1 - Cadastar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedito')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opcao Invalida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto')
    print('\n')

    nome: str = input('informe o nome do produto: ')
    preco: float = float(input('informe o numero do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('\n')
        for produto in produtos:
            print(produto)
            print('\n')
            sleep(1)
    else:
        print('Ainda nao existem produtos cadastrados.')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o codigo que deseja adicionar ao carrinho: ')
        print('\n')
        print('Produtos disponiveis')
        for produto in produtos:
            print(produto)
            print('\n')
            sleep(1)
        codigo: int = int(input())

        produto: produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho!')
                sleep(2)
                menu()

        else:
            print(f'O produto com o codigo {codigo}, nao foi encontrado')
        sleep(2)
        menu()

    else:
        print('Ainda nao existem produtos para vender!')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos do carrinho')
        
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('\n')
                sleep(1)
    else:
        print('Ainda nao existem produtos no carrinho')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('\n')
                sleep(2)
        print(f'Sua fatura e: {formata_float_str_moeda(valor_total)}')
        print('Volte sempre')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda nao existem produtos no carrinho')
    sleep(1)
    menu()


def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
