na = int(input("Número de jogadores"))
alt = 0
for i in range(na):
    a = float(input("Qual a altura dos jogadores"))
    alt+=a
print(f'{alt / na}')
    