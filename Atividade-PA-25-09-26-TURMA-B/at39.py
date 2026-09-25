poltronas = [False] * 10

while True:
    print("\nMapa de Assentos:")
    for i in range(10):
        status = "[X]" if poltronas[i] else f"[{i}]"
        print(status, end=" ")
    print()
    
    reserva = int(input("Digite o número da poltrona (0 a 9) para reservar (negativo para sair): "))
    if reserva < 0:
        break
    if 0 <= reserva <= 9:
        if poltronas[reserva]:
            print("Ocupada")
        else:
            poltronas[reserva] = True
            print("Reservada")
    else:
        print("Poltrona inválida!")