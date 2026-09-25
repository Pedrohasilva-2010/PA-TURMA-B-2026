saque = int(input("Digite o valor do saque: R$ "))

n50 = saque // 50
saque %= 50

n20 = saque // 20
saque %= 20

n10 = saque // 10
saque %= 10

n1 = saque // 1

print(f"Notas de R$ 50: {n50}")
print(f"Notas de R$ 20: {n20}")
print(f"Notas de R$ 10: {n10}")
print(f"Notas de R$ 1: {n1}")