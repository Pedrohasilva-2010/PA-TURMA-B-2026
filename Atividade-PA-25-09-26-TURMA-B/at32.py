notas = []
for i in range(5):
    nota = float(input(f"Nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
acima_da_media = 0

for nota in notas:
    if nota > media:
        acima_da_media += 1

print(f"\nMédia da turma: {media:.2f}")
print(f"Alunos com nota acima da média: {acima_da_media}")