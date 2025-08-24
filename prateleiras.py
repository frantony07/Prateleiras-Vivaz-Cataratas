import datetime
class objeto:   
    idsUsados=[]
    nomesUsados=[]
    unidadesMedidas=["0-UND(Unidade)","1-LT(Litros)","2-KG(Kilo)","3-PC(Pacote)"]

    def __init__(self,id,nome,stock,unidadeMedida,validade):
        self.id=int(id)
        self.nome=str(nome)
        self.stock=int(stock)
        self.unidadeMedida=unidadeMedida
        self.validade=validade
    
    def criarProduto():
        id_novo = objeto.criarId()
        nome_novo = objeto.criarNome()
        unidade_medida_nova = objeto.criarUnidadeMedida()
        stock_novo = objeto.criarStock()
        validade_nova = objeto.criarvalidade()
        produto = objeto(id_novo, nome_novo, stock_novo, unidade_medida_nova, validade_nova)
        return produto

    def criarId():
        while True:
            id=int(input("digite o id do produto\n"))
            if id in objeto.idsUsados:
                print("id invalido\n")
            else:
                objeto.idsUsados.append(id)
            break 
        return id
    
    def criarNome():
        while True:
            nome=str(input("digite o nome do produto\n"))
            if nome in objeto.nomesUsados:
                print("nome invalido\n")
            else:
                objeto.nomesUsados.append(nome)
                break
        return nome
    
    def criarStock():
        while True:
            stock=int(input("digite o stock\n"))
            if stock<=0:
                print("stock invalido\n")
            else: break
        return stock
    
    def criarUnidadeMedida():
        while True:
            print(objeto.unidadesMedidas)
            undMedida=int(input("escolha uma das opçoes\n"))
            if undMedida < 0 or undMedida > len(objeto.unidadesMedidas):
                print("opçao invalida\n")
            else: break
        return objeto.unidadesMedidas[undMedida-1]
    
    def criarvalidade():
        ano=objeto.validarAno()
        mes=objeto.validarMes()
        objeto.ModificarMesSiAnoForBisiestro(ano,mes)
        dia=objeto.validarDia(mes,ano)
        validadeStr=(f'{dia}/{mes}/{ano}')
        validade=datetime.strptime(validadeStr,"%d/%m/%y")
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
            if(dia>objeto.diasMes[mes-1][1]):
                print('opçao invalida\n')
            else:
                break
        return dia
    
    def ModificarMesSiAnoForBisiestro(ano,mes):
        anoBisiestro=objeto.verificarAnoBisiestroEmesFevereiroNaoUsar(ano,mes)
        if anoBisiestro == True:
            objeto.diasMes[1][1]=29

    def verificarAnoBisiestroEmesFevereiroNaoUsar(ano,mes):
        éBisiestro=objeto.verificarAnoBisiestroNaoUsar(ano)
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
    def __init__(self,):
        self.itensNaReparticao=[]
    
    def criarReparticao():
        return reparticao()

    def inserirProdutoNarepaticao(self):
        itens=objeto.criarProduto()
        self.itensNaReparticao.append(itens)

    def mostrarProdutosDaReparticao(self):

        for produto in self.itensNaReparticao:
         print(f"ID: {produto.id}, Nome: {produto.nome}, Stock: {produto.stock}, Unidade: {produto.unidadeMedida}, Validade: {produto.validade}")

            
class prateleira:

    def __init__(self):
        self.reparticao1=reparticao.criarReparticao()
        self.reparticao2=reparticao.criarReparticao()
        self.reparticao3=reparticao.criarReparticao()
        self.reparticao4=reparticao.criarReparticao()
        self.reparticao5=reparticao.criarReparticao()

    def criarPrateleira(self):
        novaPrateleira=(self.reparticao1,self.reparticao2,self.reparticao3,self.reparticao4,self.reparticao5)
        return novaPrateleira
    

   # def buscarProduto(produto,prateleiras):
    #    prateleiras=prateleira.criarPrateleira()
     #   for i, repart in enumerate(prateleiras, start=1):
      #      if produto in repart:  
       #         return  True, print(f"Produto encontrado na repartição {i}")
           

    





    
