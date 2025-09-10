def Mostrarerro(e):
    if isinstance(e, ValueError):
        print("erro na digitação de algum numero")
    elif isinstance(e , ZeroDivisionError):
        print("erro na diviçao, é imposivel divivir entre 0")