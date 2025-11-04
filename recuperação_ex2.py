num = int(input("Digite um numero: "))
result=''
original = num
while num > 0: 
    n = num % 10
    result=result+str(n)
    num = num // 10
if original == int(result):
    print(f'Numero é um palindromo:')
else: 
    print(f'Numero não é um palindromo: ')
print(result)
