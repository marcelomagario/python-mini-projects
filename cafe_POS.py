"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""

# from collections import Counter
def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""
    especificacoes = ['Cachorro Quente', 'Bauru Simples', 'Bauru com Ovo', 'Hamburger', 'Cheeseburger', 'Refrigerante']
    codigos = ['100', '101', '102', '103', '104', '105']
    precos_unitario = [1.2, 1.3, 1.5, 1.2, 1.0]
    count_100, count_101, count_102, count_103, count_104, count_105 = 0, 0, 0, 0, 0, 0
    for i in range(len(itens)):
        if itens[i][0] == '100':
            count_100 += itens[i][1]
        elif itens[i][0] == '101':
            count_101 += itens[i][1]
        elif itens[i][0] == '102':
            count_102 += itens[i][1]
        elif itens[i][0] == '103':
            count_103 += itens[i][1]
        elif itens[i][0] == '104':
            count_104 += itens[i][1]
        elif itens[i][0] == '105':
            count_105 += itens[i][1]
    qtdes_itens = [count_100, count_101, count_102, count_103, count_104, count_105]

    for especificacao, codigo, preco_unitario, qtde_iten in zip(especificacoes, codigos, precos_unitario, qtdes_itens):
        if qtde_iten != 0:
            print(f'{especificacao}  | {codigo}, {preco_unitario} | {qtde_iten} | {preco_unitario * qtde_iten}')


    # quantidade_por_produtos = {}
    # for i in range(len(itens)):
    #     for k, v in quantidade_por_produtos.items():
    #         quantidade_por_produtos[k] = v
    # print(quantidade_por_produtos)

