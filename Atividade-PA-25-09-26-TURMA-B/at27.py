vetor = []
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    vetor.append(num)

print("\nNúmeros PARES digitados:")
for num in vetor:
    if num % 2 == 0:
        print(num)