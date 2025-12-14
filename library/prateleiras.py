from datetime import datetime
from erro.errorCode import MostrarErro
class iten:
    """
    Esta classe e a responsavel da criação dos itens.
    cada item contem:
    Uma unico Id.
    Um unico nome.
    Uma unidade de medida na qual o usuario consegue escolher entre unidade, litro, kilograma ou  pacote.
    O stock do producto (o qual nao pode ser menor a 0).
    A validade do produto(data de vencimento do produto).
    """
    idsUsados=[]
    #Este array almacena os ids de todos os itens criados 
    nomesUsados=[]
    #Este array almacena os nomes de todos os itens criados
    unidadesMedidas=["0-UND(Unidade)","1-LT(Litros)","2-KG(Kilo)","3-PC(Pacote)"]
    #este array almacena as unidades de medida 
    def __init__(self,id,nome,stock,unidadeMedida,validade,stockMinimo):
        self.id=int(id)
        self.nome=str(nome)
        self.stock=int(stock)
        self.unidadeMedida=str(unidadeMedida)
        self.validade=str(validade)
        self.stockMinimo=int(stockMinimo)
        self.stockEstaMinimo=False
    
    def criarProduto():
        id_novo = iten.criarId()
        nome_novo = iten.criarNome()
        unidade_medida_nova = iten.criarUnidadeMedida()
        stock_novo = iten.criarStock()
        validade_nova = iten.criarvalidade()
        stockMinimo_novo= iten.criarStockMinimo()
        produto = iten(id_novo, nome_novo, stock_novo, unidade_medida_nova, validade_nova,stockMinimo_novo)
        return produto

    def criarId():
        while True:
            try:
                id=int(input("digite o id do produto\n"))
                
            except Exception as e:
                MostrarErro(e)

            else:
                if id in iten.idsUsados:
                    print("id invalido\n")
                else:
                    iten.idsUsados.append(id)
                    print("Id cadastrado con sucesso ")
                    return id

    
    def criarNome():
        while True:
            try:
                nome=str(input("digite o nome do produto\n")) 

            except Exception as e:
                MostrarErro(e)

            else:
                if nome in iten.nomesUsados:
                    print("nome invalido\n")
                else:
                    iten.nomesUsados.append(nome)
                    print("nome cadastrtado com sucesso ")
                    return nome
    
    def criarStock():
        while True:
            try:
                stock=int(input("digite o stock\n"))
                
            except Exception as e :
                MostrarErro(e)

            else:
                if stock<0:
                    print("stock invalido\n")
                else: 
                    print("stock criado com sucesso")
                    return stock
    
    def criarUnidadeMedida():
        while True:
            try:
                print(iten.unidadesMedidas)
                undMedida=int(input("escolha uma das opçoes\n"))
    
            except Exception as e:
                MostrarErro(e)
            
            else:
                if undMedida < 0 or undMedida > len(iten.unidadesMedidas):
                    print("opçao invalida\n")
                else:
                    print("Unidade de medida cadastrada com sucesso")
                    return iten.unidadesMedidas[undMedida-1]

    def criarStockMinimo():
        while True:
            try:
                stockMinimo=int(input("digite o stock minimo do produto\n"))

            except Exception as e:
                MostrarErro(e)

            else:
                if stockMinimo < 0:
                    print("stock minimo invalido")
                else:
                    print("stock minimo cadastrado com sucesso")
                    return stockMinimo
                       
    def criarvalidade():
        ano=iten.validarAno()
        mes=iten.validarMes()
        iten.ModificarMesSiAnoForBisiestro(ano,mes)
        dia=iten.validarDia(mes,ano)
        validadeStr=(f'{dia}/{mes}/{ano}')
        validade=datetime.strptime(validadeStr,"%d/%m/%Y")
        return validade

    diasMes={
        1 : 31 ,
        2 : 28 ,
        3 : 31 ,
        4 : 30 ,
        5 : 31 ,
        6 : 30 ,
        7 : 31 ,
        8 : 31 ,
        9 : 30 ,
        10 : 31 ,
        11 : 30 ,
        12 : 31 
    }
    def validarAno():
        while True:
            try:
                ano=int(input('digite o ano de vencimento\n'))
                agora=datetime.now().year

            except Exception as e:
                MostrarErro(e)
            
            else:
                if ano >= agora:
                    print("Ano cadastrado com sucesso")
                    return ano
                else:
                    print("data invalida")


    def validarMes():
        while True:
            try:
                mes=int(input('digite o mes de vencimento em numero\n'))
                
            except Exception as e:
                MostrarErro(e)
            
            else:
                if mes>12 or mes<1:
                    print('opcao invalida\n')
                else:
                    print("mes cadastrado com sucesso")
                    return mes
        
    
    def validarDia(mes,ano):
        while True:
            try:
                dia=int(input('digite o dia de vencimento\n'))
                
            except Exception as e:
                MostrarErro(e)

            else: 
                if(dia>iten.diasMes[mes]):
                    print('opçao invalida\n')
                else:
                    print("dia cadastrado com sucesso")
                    return dia
            
    
    def ModificarMesSiAnoForBisiestro(ano,mes):
        anoBisiestro=iten.verificarAnoBisiestroEmesFevereiroNaoUsar(ano,mes)
        if anoBisiestro == True:
            iten.diasMes[2]=29

    def verificarAnoBisiestroEmesFevereiroNaoUsar(ano,mes):
        éBisiestro=iten.verificarAnoBisiestroNaoUsar(ano)
        if mes==2 and éBisiestro==True:
            return True
        else:
            return False
    
    def verificarAnoBisiestroNaoUsar(ano):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return True
        else:
            return False   
class prateleira:
    """
    esta classe e a responsavel da administração das repartições.
    cada prateleira conta com 5 repartiçoes as quais conten um array que almacema itens.
    """

    def __init__(self):

        self.itensNaPrateleira=[]

    def criarPrateleira(self):
        return self.reparticoes