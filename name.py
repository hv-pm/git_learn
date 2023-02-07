name = input("Insira seu primeiro nome: ")

if not name.isdigit():

    if len(name) <= 4:
        print("Seu nome é curto.")
    elif len(name) >= 5 and len(name) <= 6:
        print("Seu nome tem tamanho normal.")
    elif len(name) >= 6:
        print("Seu nome é muito grande.")

else:
    print("Insira um nome.")

print("")
input("Pressione ENTER para encerrar.")