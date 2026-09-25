vetor = []
for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    vetor.append(num)

print("\nÍndices e Valores:")
for i in range(len(vetor)):
    print(f"Posição {i}: {vetor[i]}")