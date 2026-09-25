lista = [12, 45, 7, 23, 89, 34, 56, 90]
busca = int(input("Digite um número para buscar: "))

encontrado = False
for i in range(len(lista)):
    if lista[i] == busca:
        print(f"Número encontrado na posição (índice) {i}!")
        encontrado = True
        break

if not encontrado:
    print("Número não encontrado na lista.")