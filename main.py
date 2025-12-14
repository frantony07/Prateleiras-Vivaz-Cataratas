from library.prateleiras import prateleira
from library.prateleiras import iten
from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Any , Callable
from erro.errorCode import MostrarErro
from library.programingClean import limparTela , pause
import os


quantidadeDePrateleiras=5

almoxarifado= [prateleira() for _ in range(quantidadeDePrateleiras)]


def loopDeBusqueda(fuction:Callable,produtoBuscado:Any,booleanValue:bool):
    """
    este loop e responsavel por percorrer todas as prateleiras do almoxarifado na buscaqueda de algum item .
    Retornara True se encontar o item 
    Args:
        function (fuction): Função usada para aplicar a busca em cada item.
        produtoBuscado (Any): Nome ou identificador do produto a ser buscado.
        booleanValue (bool): Indica se o produto foi encontrado (True) ou não (False).

    Returns:
            bool: Retorna True se encontrar o item.
    """
    for i , reparticao in enumerate(almoxarifado):                   
        for j , itens in enumerate(reparticao.itensNaPrateleira):
             booleanValue = fuction(itens, produtoBuscado, booleanValue, i, j)
    return booleanValue

def buscarProdutos():
    try:
        produtoBuscado=str(input("digita o produto que deseja procurar\n"))
        
    except Exception as e:
        MostrarErro(e)
    
    else:
        booleanValue=False
        booleanValue = loopDeBusqueda(funçãoDeBusqueda, produtoBuscado, booleanValue)

        if not booleanValue:
            print("Produto não encontrado")
            pause()

        

def funçãoDeBusqueda(itens:object, produtoBuscado:Any, booleanValue:bool, i:int, j:int):
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
        
        print(f"Produto {produtoBuscado} achado na prateleira {i+1}")
        boleanValue = True
    return boleanValue
    

def adicionarProduto():
    itens=iten.criarProduto()
    prateleira=selecionarPrateleira()
    almoxarifado[prateleira].itensNaPrateleira.append(itens)
    print("produto cadastrado com sucesso!\n")
    pause()

def selecionarPrateleira():
    while True:
        try:
            prateleira=int(input("digite a prateleira na que deseja adicionar o produto\n"))-1
            if prateleira<=len(almoxarifado):
                return prateleira
    
        except Exception as e:
            MostrarErro(e)

def produtosProximos_a_Vencer():
    try:
        agora=datetime.now()
        vencimentoCurto=agora + relativedelta(month=3)
        booleanValue=False
        print("Produtos proximos a vencer\n")
        booleanValue=loopDeBusqueda(fuctionVencimento,vencimentoCurto,booleanValue)   
    except Exception as e:
        MostrarErro(e)
    
    else:
        if not booleanValue:
            print("nenhum produto proximo a vencer encontrado\n")
            pause()

def fuctionVencimento(itens:object, produtoBuscado:Any, booleanValue:bool, i:int, j:int):
    """
    esta função e responsavel por mostrar os produtos que estan com o stock baixo no sistema.
    a função tem que ser passada como parametro na função loopDeBusqueda.
    Args:
        itens (object): e o objeto que esta dispovel na prateleira.
        produtoBuscado (Any):e o produto que o usuario esta procurando.
        booleanValue (bool):identifica se o produto foi encontrado.
        i (int): e a prateleira.
        Returns:
        bool: Retorna True se encontrar o item."""
    try:
        booleanValue = True
        if itens.validade <= produtoBuscado:
            print(f"{itens.nome} da prateleira {i} vai vencer em {itens.validade.date()}")
        
    except Exception as e:
        MostrarErro(e)

    else:
        return booleanValue

def fuctionStockBaixo(itens:object, produtoBuscado:Any, booleanValue:bool, i:int, j:int):
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
        bool: Retorna True se encontrar o item. """
    try:
        booleanValue=True
        if itens.stock<= itens.stockMinimo:
            itens.stockEstaMinimo=True
            print(f"{itens.nome}, da prateleira{i+1} conta com {itens.stock} de stock")            
    except Exception as e:
        MostrarErro(e)
    else:
        return booleanValue

def produtoComStockBaixo():
    try:
        booleanValue=False
        parametro="não e preciso"
        print("produtos com stock baixo\n")
        booleanValue=loopDeBusqueda(fuctionStockBaixo,parametro,booleanValue)
        pause()
    except Exception as e:
        MostrarErro(e)
    else:
        if not booleanValue:
            print("nenhum produto encontrado")
            pause()


def main():
    while True:
        try:
            print("""        Bem vindo ao menu principal
            1.Buscar produto
            2.Adicionar produtos
            3.Produtos com vencimento curto
            4.Produtos com estoque baixo
            5.Administrar prateleiras
            6.sair do sistema""")
            opcao=int(input('escolhe uma das opçoes\n'))
            match opcao:
                case 1: buscarProdutos()
                case 2: adicionarProduto()
                case 3: produtosProximos_a_Vencer()
                case 4: produtoComStockBaixo()
                case 5: break
                case _:
                    print('opçao invalida')
                    pause()
                
            limparTela()
        except Exception as e:
            MostrarErro(e)
            
if __name__ == "__main__":
    main()


