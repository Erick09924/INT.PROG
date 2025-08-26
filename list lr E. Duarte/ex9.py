np = int(input("Digite um númro: "))
resto = 0
for i in range(1,(np+1)):
    if np%i ==0:
        resto+=1
if resto ==2:
    print(f'Esse número é primo')
else:
    print(f'Esse número não é primo')


