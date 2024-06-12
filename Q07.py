nome = input("Nome do estudante: ")
materia = input("Qual é a matéria?: ")
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
m = (n1 + n2)/2
if m >= 6:
    situacao = "aprovado"
else:
    situacao = "reprovado"
print(f'{nome} está {situacao} na disciplina de {materia}')
