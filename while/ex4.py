quantidade = int(input("Digite a quantidade de jogadores "))
jogador=1
soma = 0
while jogador <= quantidade:
    altura = float(input(f'Digite a altura do jogador {jogador}: '))
    soma+=altura
    jogador+=1    
    media = soma / quantidade
print(f'{media:.2f}')
