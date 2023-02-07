value = input("Insira um número inteiro: ")

if value.isdigit():
    value = int(value)
    leftover = value % 2

    if leftover == 0:
        print(f"{value} é par.")
    else:
        print(f"{value} é impar.")

else:
    print("Por favor insira um número.")

print("")
input("Pressione ENTER para encerrar.")