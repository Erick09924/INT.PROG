qndt_reprov = 0
qndt_aprov = 0
maior = 0
menor = 10
for i in range(1,11):
    n1 = float(input("Nota dos aluno n1"))
    n2 = float(input("Nota dos aluno n2 "))
    n3 = float(input("Notas do aluno n3 "))
    media =((n1 + n2 + n3) /3)
    if maior>media:
        media=maior
    elif menor<media:
        media+menor
    if media >= 6:
        qndt_aprov+=1
    else:
        qndt_reprov+=1
print(f"Quantidade de alunos aprovados{qndt_aprov}")
print(f"Quantidade de alunos reprovados{qndt_reprov}")
print(f'maior média: {maior}')
print(f'menor média: {menor}')

