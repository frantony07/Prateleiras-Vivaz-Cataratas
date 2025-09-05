from datetime import datetime
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
    def __init__(self,id,nome,stock,unidadeMedida,validade):
        self.id=int(id)
        self.nome=str(nome)
        self.stock=int(stock)
        self.unidadeMedida=unidadeMedida
        self.validade=validade
    
    def criarProduto():
        id_novo = iten.criarId()
        nome_novo = iten.criarNome()
        unidade_medida_nova = iten.criarUnidadeMedida()
        stock_novo = iten.criarStock()
        validade_nova = iten.criarvalidade()
        produto = iten(id_novo, nome_novo, stock_novo, unidade_medida_nova, validade_nova)
        return produto

    def criarId():
        while True:
            id=int(input("digite o id do produto\n"))
            if id in iten.idsUsados:
                print("id invalido\n")
            else:
                iten.idsUsados.append(id)
                break 
        return id
    
    def criarNome():
        while True:
            nome=str(input("digite o nome do produto\n"))
            if nome in iten.nomesUsados:
                print("nome invalido\n")
            else:
                iten.nomesUsados.append(nome)
                break
        return nome
    
    def criarStock():
        while True:
            stock=int(input("digite o stock\n"))
            if stock<0:
                print("stock invalido\n")
            else: break
        return stock
    
    def criarUnidadeMedida():
        while True:
            print(iten.unidadesMedidas)
            undMedida=int(input("escolha uma das opçoes\n"))
            if undMedida < 0 or undMedida > len(iten.unidadesMedidas):
                print("opçao invalida\n")
            else: break
        return iten.unidadesMedidas[undMedida-1]
    
    def criarvalidade():
        ano=iten.validarAno()
        mes=iten.validarMes()
        iten.ModificarMesSiAnoForBisiestro(ano,mes)
        dia=iten.validarDia(mes,ano)
        validadeStr=(f'{dia}/{mes}/{ano}')
        validade=datetime.strptime(validadeStr,"%d/%m/%Y")
        return validade

    diasMes=[
        ["janeiro", 31 ],
        ["fevereiro", 28 ],
        ["março", 31 ],
        ["abril", 30 ],
        ['maio', 31 ],
        ["junho", 30 ],
        ['julho', 31 ],
        ["agosto", 31 ],
        ["setembro", 30 ],
        ["outubro", 31 ],
        ["novembro", 30 ],
        ["dezembro", 31 ]
    ]
    def validarAno():
        ano=int(input('digite o ano de vencimento\n'))
        return ano
    
    def validarMes():
        while True:
            mes=int(input('digite o mes de vencimento em numero\n'))
            if mes>12 or mes<1:
                print('opcao invalida\n')
            else: break
        return mes
    
    def validarDia(mes,ano):
        while True:
            dia=int(input('digite o dia de vencimento\n'))
            if(dia>iten.diasMes[mes-1][1]):
                print('opçao invalida\n')
            else:
                break
        return dia
    
    def ModificarMesSiAnoForBisiestro(ano,mes):
        anoBisiestro=iten.verificarAnoBisiestroEmesFevereiroNaoUsar(ano,mes)
        if anoBisiestro == True:
            iten.diasMes[1][1]=29

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
class reparticao:
    """
    Esta classe e a responsavel pelo  almacenamento dos  itens 
    """
    def __init__(self,):
        self.itensNaReparticao=[]
    
    def criarReparticao():
        return reparticao()

class prateleira:
    """
    esta classe e a responsavel da administração das repartições.
    cada prateleira conta com 5 repartiçoes as quais conten um array que almacema itens.
    """

    def __init__(self):

        self.reparticoes=[reparticao.criarReparticao() for _ in range(5)]

    def criarPrateleira(self):
        return self.reparticoes
           





    
