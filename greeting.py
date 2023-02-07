print("Insira a hora atual usando o formato 24 horas e seja cumprimentado")
print("")

currentTime = input("Insira a hora atual: ")

if currentTime.isdigit():
    if int(currentTime) >= 0 and int(currentTime) <= 11:
        print("Bom dia!")
    elif int(currentTime) >= 12 and int(currentTime) <= 17:
        print("Boa tarde!")
    elif int(currentTime) >= 18 and int(currentTime) <= 23:
        print("Boa noite!")
    elif int(currentTime) == 24:
        print("É madrugada!")
else:
    print("Por favor, insira um número.")

print("")
input("Pressione ENTER para encerrar.")