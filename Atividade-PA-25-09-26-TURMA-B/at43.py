while True:
    nota = float(input("Digite uma nota de 0 a 10: "))
    if nota >= 0 and nota <= 10:
        print("Nota válida!")
        break
    else:
        print("Erro: A nota é inválida. Tente novamente.")