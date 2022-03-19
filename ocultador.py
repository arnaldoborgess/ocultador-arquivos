import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada: ")

atributo_ocultar = 0x02 # define o atributo do arquivo oculto

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)# chama a dll que pertique o arquivo fique oculto
if retorno:
    print("Arquivo  foi ocultado")
else:
    print("Arquivo não foi ocultado.")