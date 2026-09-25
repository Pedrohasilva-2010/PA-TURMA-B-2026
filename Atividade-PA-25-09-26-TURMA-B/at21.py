soma = 0
quantidade = 0

numero = int(input("Digita um número (0 para parar): "))

while numero != 0:
    soma = soma + numero
    quantidade = quantidade + 1
    numero = int(input("Digita outro número (0 para parar): "))

print("Quantidade de números:", quantidade)
print("Soma total:", soma)