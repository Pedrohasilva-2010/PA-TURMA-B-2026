import random

computador = random.randint(1, 10)
acertou = False
tentativas = 0

while not acertou:
    jogador = int(input("Tente adivinhar (1 a 10): "))
    tentativas = tentativas + 1
    
    if jogador == computador:
        acertou = True
        print(f"Você acertou com {tentativas} tentativas!")
    elif jogador < computador:
        print("Maior...")
    else:
        print("Menor...")