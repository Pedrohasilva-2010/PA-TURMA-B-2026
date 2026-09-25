velocidade = float(input("Qual a velocidade do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado! O valor é R$ {multa:.2f}")
else:
    print("Boa viagem!")