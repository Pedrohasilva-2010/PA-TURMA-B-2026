import random

campo = [0] * 10
minas = random.sample(range(10), 3)
for pos in minas:
    campo[pos] = 1

passos = 0
perdeu = False

while passos < 5:
    pos = int(input(f"Passo {passos+1}/5 - Escolha uma posição (0 a 9): "))
    if campo[pos] == 1:
        print("BOOM! Você pisou em uma mina e perdeu.")
        perdeu = True
        break
    else:
        print("Ufa! Posicão segura.")
        passos += 1

if not perdeu:
    print("Parabéns! Você sobreviveu aos 5 passos e ganhou!")