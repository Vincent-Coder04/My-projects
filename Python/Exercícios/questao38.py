import platform

def exibir_sistema():
    sistema = platform.system()  
    versao = platform.version()  
    release = platform.release()  

    print(f"Sistema Operacional: {sistema}")
    print(f"Versão: {versao}")
    print(f"Release: {release}")

exibir_sistema()