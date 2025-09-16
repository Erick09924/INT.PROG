qndt=0
num=0
soma=0
while num < 20:
    n = int(input("Escreva um valor inteiro: "))
    if n >0:
        soma+=n
    else:
        qndt+=1
    num +=1
print('Soma dos números positivos {} quantidade dos números negativos {}'.format(soma, qndt))
