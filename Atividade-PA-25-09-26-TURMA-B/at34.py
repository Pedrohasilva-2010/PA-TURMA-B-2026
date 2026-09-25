votos = [0, 0, 0, 0, 0]

while True:
    voto = int(input("1-João | 2-Maria | 3-José | 4-Nulo | 5-Branco | 0-Encerrar: "))
    if voto == 0:
        break
    if 1 <= voto <= 5:
        votos[voto - 1] += 1
    else:
        print("Opção inválida!")

print("\n--- Resultado Final ---")
candidatos = ["João", "Maria", "José", "Nulo", "Branco"]
for i in range(5):
    print(f"{candidatos[i]}: {votos[i]} voto(s)")

votos_validos = votos[:3]
maior_voto = max(votos_validos)

if votos_validos.count(maior_voto) > 1:
    print("Empate na votação!")
else:
    vencedor_idx = votos_validos.index(maior_voto)
    print(f"Vencedor: {candidatos[vencedor_idx]}")