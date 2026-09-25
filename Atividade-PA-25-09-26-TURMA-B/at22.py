primeiro = int(input("Digite o 1º número: "))
maior = primeiro
menor = primeiro

for i in range(4):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O MAIOR foi {maior}")
print(f"O MENOR foi {menor}")