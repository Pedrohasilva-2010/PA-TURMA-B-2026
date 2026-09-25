frase = input("Digite uma frase: ")

palavras = len(frase.split())
qtd_a = 0

for char in frase:
    if char in 'aA':
        qtd_a += 1

print(f"Quantidade de palavras: {palavras}")
print(f"Quantidade de letras 'A'/'a': {qtd_a}")