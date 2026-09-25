vetor = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(num)

print(f"\nOrdem digitada: {vetor}")

print("Ordem inversa: ", end="")
for i in range(len(vetor) - 1, -1, -1):
    print(vetor[i], end=" ")
print()