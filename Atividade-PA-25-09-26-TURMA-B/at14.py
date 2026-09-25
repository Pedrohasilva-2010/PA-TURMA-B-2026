n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
print("Escolha a operação: 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão")
opcao = int(input("Opção: "))

if opcao == 1:
    print(f"Resultado: {n1 + n2}")
elif opcao == 2:
    print(f"Resultado: {n1 - n2}")
elif opcao == 3:
    print(f"Resultado: {n1 * n2}")
elif opcao == 4:
    print(f"Resultado: {n1 / n2}")
else:
    print("Opção inválida.")