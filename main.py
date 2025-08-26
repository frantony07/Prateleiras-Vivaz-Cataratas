from prateleiras import prateleira
from prateleiras import objeto
import os
import platform 
import datetime

def limparTela():
    os.system("pause")
    sistema=platform.system()
    if sistema=="Windows":
        os.system("cls")
    else:
        os.system("clear")

P1=prateleira()
P2=prateleira()
P3=prateleira()
P4=prateleira()
P5=prateleira()

almoxarifado=[
    P1.criarPrateleira(),
    P1.criarPrateleira(),
    P1.criarPrateleira(),
    P1.criarPrateleira(),
    P1.criarPrateleira()
]

def buscarProdutos():
    produtoBuscado=input("digita o produto que deseja procurar\n")
    realizarBusqueda(produtoBuscado)

def realizarBusqueda(produto):
    for i in range(len(almoxarifado)):                
        for j in range(len(almoxarifado[i])):         
            if produto in almoxarifado[i][j].itensNaReparticao :
                print(f"Produto {produto} achado na prateleira {i+1} na repartiçao {j+1}\n")
                return True

    print("produto nao achado\n")

def adicionarProduto():
    itens=objeto.criarProduto()
    prateleira=int(input("digite a prateleira na que deseja adicionar o produto\n"))-1
    repartiçao=int(input("digite a reparticao que deseja adicionar o produto\n"))-1
    almoxarifado[prateleira][repartiçao].append(itens)
    print("produto cadastrado com sucesso!\n")

def produtoComStockBaixo():
    encontrado=False
    print("produtos com stock baixo\n")
    for i in range(len(almoxarifado)):
        for j in range(len(almoxarifado[i])):
            for itens in almoxarifado[i][j].itensNaReparticao:
                if itens.stock<= 5:
                    print( almoxarifado[i][j].itensNaReparticao,f"na prateleira{i} repartição{j}")
                    
                    encontrado=True
    if not encontrado:
        print("nenhum produto com stock baixo\n")

def produtosProximos_a_Vencer():
    vencimentoCurto=objeto.criarvalidade()
    encontrado=False
    print("Produtos proximos a vencer\n")
    for i in range(len(almoxarifado)):
        for j in range(len(almoxarifado[i])):
            for itens in almoxarifado[i][j].itensNaReparticao:
                if itens.validade==vencimentoCurto:
                    print( almoxarifado[i][j].itensNaReparticao,f"da prateleira{i} na repartição{j}")
                    encontrado=True
    if not encontrado:
        print("nenhum produto proximo a vencer encontrado\n")



        

def main():
    while True:
        print("""        Bem vindo ao menu principal
          1.Buscar produto
          2.Adicionar produtos
          3.Produtos com vencimento curto
          4.Produtos com estoque baixo
          5.Administrar prateleiras
          6.sair do sistema\n
          """)
        opcao=int(input('escolhe uma das opçoes\n'))
        match opcao:
            case 1: buscarProdutos()
            case 2: adicionarProduto()
            case 3: produtosProximos_a_Vencer
            case 4: produtoComStockBaixo()
        limparTela()
            


if __name__ == "__main__":
    main()


