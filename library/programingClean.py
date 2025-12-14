import os
import platform 

def limparTela():
    pause()
    sistema=platform.system()
    if sistema=="Windows":
        os.system("cls")
    else:
        os.system("clear")

def pause():
    input("Pressione Enter para continuar...")