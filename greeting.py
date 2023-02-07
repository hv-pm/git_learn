currentTime = input("Insira a hora atual: ")

if currentTime.isdigit():
    if int(currentTime) >= 0 and int(currentTime) <= 11 or int(currentTime) == 24:
        print("Bom dia!")
    elif int(currentTime) >= 12 and int(currentTime) <= 17:
        print("Boa tarde!")
    elif int(currentTime) >= 18 and int(currentTime) <= 23:
        print("Boa noite!")
else:
    print("Por favor, insira um número.")

print("")
input("Pressione ENTER para encerrar.")