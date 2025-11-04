# Recuperação: Arthur , Nicollas , Erick
pares = 0
impares = 0
num = int(input("Digite um numero: "))
while num<=0:
    print("digite o número novamente. ")
    num = int(input("Digite um numero: "))
while num != 0:    
    digito = num % 10
    if digito % 2 == 0:
        pares+=1
    else:
        impares+=1
    num = num // 10
print(f'A quantidade de números pares é de {pares}')
print(f'A quantidade de números impares é de {impares}')




