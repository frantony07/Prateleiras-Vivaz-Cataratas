from prateleiras import prateleira
from prateleiras import iten
import os
import platform 
from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Any 

def limparTela():
    os.system("pause")
    sistema=platform.system()
    if sistema=="Windows":
        os.system("cls")
    else:
        os.system("clear")


quantidadeDePrateleiras=5

almoxarifado= [prateleira() for _ in range(quantidadeDePrateleiras)]


def loopDeBusqueda(fuction:function,produtoBuscado:Any,booleanValue:bool):
    """
    este loop e responsavel por percorrer todas as prateleiras do almoxarifado na buscaqueda de algum item ou dado.
    Retornara True se encontar o item ou o dado
    Args:
        function (fuction): Função usada para aplicar a busca em cada item.
        produtoBuscado (Any): Nome ou identificador do produto a ser buscado.
        booleanValue (bool): Indica se o produto foi encontrado (True) ou não (False).

    Returns:
            bool: Retorna True se encontrar o item.
    """
    for i , prateleira in enumerate(almoxarifado):                
        for j , reparticoes in enumerate(prateleira.reparticoes):    
            for n , itens in enumerate(reparticoes.itensNaReparticao):
                 booleanValue = fuction(itens, produtoBuscado, booleanValue, i, j, n)
    return booleanValue

def buscarProdutos():
    produtoBuscado=input("digita o produto que deseja procurar\n")
    booleanValue=False
    booleanValue = loopDeBusqueda(funçãoDeBusqueda, produtoBuscado, booleanValue)

    if not booleanValue:
        print("Produto não encontrado")

def funçãoDeBusqueda(itens:object, produtoBuscado:Any, booleanValue:bool, i:int, j:int, n:int):
    """
    esta função e a responsavel por verificar se o produto que estamos buscando esta existe.
    a função tem que ser passada como parametro na função loopDeBusqueda.
    Args:
        itens (object): e o objeto que esta dispovel na prateleira.
        produtoBuscado (Any):e o produto que o usuario esta procurando.
        booleanValue (bool):identifica se o produto foi encontrado.
        i (int): e a prateleira.
        j (int): e a repartição

    Returns:
        bool: Retorna True se encontrar o item.

    """
    if produtoBuscado in itens.nome:
        print(f"Produto {produtoBuscado} achado na prateleira {i+1}, repartição {j+1}")
        boleanValue = True
    return boleanValue
    

def adicionarProduto():
    itens=iten.criarProduto()
    prateleira=selecionarAprateleira()
    repartiçao=selecionarAreparticao()
    almoxarifado[prateleira].reparticoes[repartiçao].itensNaReparticao.append(itens)
    print("produto cadastrado com sucesso!\n")

def selecionarAreparticao():
    while True:
        repartiçao=int(input("digite a reparticao que deseja adicionar o produto\n"))-1
        if repartiçao <=5:
             break
        else:
            print("opcao invalida tente novamente ") 
    return repartiçao

def selecionarAprateleira():
    while True:
        prateleira=int(input("digite a prateleira na que deseja adicionar o produto\n"))-1
        if prateleira<=len(almoxarifado):
            break
    return prateleira


def produtosProximos_a_Vencer():
    agora=datetime.now()
    vencimentoCurto=agora + relativedelta(month=3)
    booleanValue=False
    print("Produtos proximos a vencer\n")
    booleanValue=loopDeBusqueda(fuctionVencimento,vencimentoCurto,booleanValue)       
    if not booleanValue:
        print("nenhum produto proximo a vencer encontrado\n")

def fuctionVencimento(itens, produtoBuscado, booleanValue, i, j, n):
     if itens.validade <= produtoBuscado:
        print(f"{itens.nome} da prateleira {i} na repartição {j} vai vencer em {itens.validade.date()}")
        booleanValue = True
        return booleanValue


def fuctionStockBaixo(itens:object, produtoBuscado:Any, booleanValue:bool, i:int, j:int, n:int):
    """
    esta função e a responsavel do controle de estoque.
    ela mostra na tela todos os produtos que estejan com menos de 5 unidades
    Args:
        itens (object): e o objeto que esta dispovel na prateleira.
        produtoBuscado (Any):e o produto que o usuario esta procurando.
        booleanValue (bool):identifica se o produto foi encontrado.
        i (int): e a prateleira.
        j (int): e a repartição

    Returns:
        bool: Retorna True se encontrar o item. 
    """
    if itens.stock<= 5:
        print( almoxarifado[i][j].itensNaReparticao,f"na prateleira{i} repartição{j}")            
        booleanValue=True
        return booleanValue
    
def produtoComStockBaixo():
    booleanValue=False
    print("produtos com stock baixo\n")
    booleanValue=loopDeBusqueda(fuctionStockBaixo,"não e preciso",booleanValue)
    if not booleanValue:
        print("nenhum produto encontrado")



def main():
    while True:
        print("""        Bem vindo ao menu principal
          1.Buscar produto
          2.Adicionar produtos
          3.Produtos com vencimento curto
          4.Produtos com estoque baixo
          5.Administrar prateleiras
          6.sair do sistema
          """)
        opcao=int(input('escolhe uma das opçoes'))
        match opcao:
            case 1: buscarProdutos()
            case 2: adicionarProduto()
            case 3: produtosProximos_a_Vencer()
            case 4: produtoComStockBaixo()
        limparTela()
            

if __name__ == "__main__":
    main()


