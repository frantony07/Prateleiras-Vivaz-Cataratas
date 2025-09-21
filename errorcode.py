def MostrarErro(e):
    mensagemDeErro={
        ValueError:"erro na digitação de algum numero",
        ZeroDivisionError:"erro na diviçao, é imposivel divivir entre 0",
        NameError:"alguma variavel usada nao foi definida",
        TypeError:"Tipo de dado ingresado, não e valido ",
        ImportError:"erro na importação",
        MemoryError: "memoria cheia"
    }
    for erroDetetado , msg in mensagemDeErro.items():
        if isinstance(e , erroDetetado):
            print(msg)
            break
    else:
        print(f"erro inesperado {e}")
        
    
