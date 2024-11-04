n = int(input("Quantas pessoas você deseja informar a idade? "))
soma_idades = 0

for i in range(n):
    idade = int(input(f"Informe a idade da pessoa {i + 1}: "))
    soma_idades += idade

media_idade = soma_idades / n
print(f"A média de idade da turma é: {media_idade:.2f}")

if media_idade <= 25:
    print("A turma é jovem.")
elif 26 <= media_idade <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")