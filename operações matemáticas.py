print ("                 MENU          ")

print("Escolha uma dessas quatro operações matemáticas abaixo! " )
print(" 1 = par ou ímpar" )
print(" 2 = adição")
print(" 3 = subtração")
print(" 4 = multiplicação")
print(" 5 = divisão")
print(" 6 = fatorial")
print(" 7 = número_primo ")
print(" Digite 'Sair' para sair")
om = (input("Escreva a operação desejada em números: "))
while om !="Sair":
    if om == "2":
        n1=int(input("Digite o primeiro número"))
        n2=int(input("Digite o segundo número"))
        print(f' A soma dos números é igual {n1+n2}')
    elif om == "3":
        n1=int(input("Digite o primeiro número"))
        n2=int(input("Digite o segundo número"))
        print(f'A subtração dos números é igual {n1-n2}')
    elif om == "4":
        n1=int(input("Digite o primeiro número"))
        n2=int(input("Digite o segundo número"))
        print(f'A multiplicação dos números é igual {n1-n2}')
    elif om == "5":
        n1=int(input("Digite o primeiro número"))
        n2=int(input("Digite o segundo número"))
        print(f'A divisão dos números é igual {n1-n2}')
    elif om == "1":
        n = input("Digite um número ")
        if n == 2:
            if n %2 == 0:
             print("Esse número é par. ")
        else: 
            print(" Esse número é ímpar. ")
    elif om == "6":
        mult = 1
        nf = input("Digite um número")
        if nf == 2: 
            for i in range (1,nf+1):
                mult = mult*i
        print(" O fatorial do número é ",mult )
    elif om == "7":
        n = input("Digite um número ")
        resto = 0
        for e in range(1,n+1):
            if  n%e==0:
                resto+=1
        if resto == 2:   
                print("Esse número é primo")
        else :
                print("Esse número não é primo")
             
    print("-------------------------------------------------------------------------------------------")
    print ("                 MENU          ")
    print("Escolha uma dessas quatro operações matemáticas abaixo! " )
    print(" 1 = par ou ímpar" )
    print(" 2 = adição")
    print(" 3 = subtração")
    print(" 4 = multiplicação")
    print(" 5 = divisão")
    print(" 6 = fatorial")
    print(" 7 = número_primo ")
    print(" Digite 'Sair' para sair")
    om = (input("Escreva a operação desejada em números: "))




       

    
    