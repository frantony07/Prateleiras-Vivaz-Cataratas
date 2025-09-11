import os
import platform 

def limparTela():
    os.system("pause")
    sistema=platform.system()
    if sistema=="Windows":
        os.system("cls")
    else:
        os.system("clear")