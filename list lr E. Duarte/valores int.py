pos = 0
neg = 0 
for v in range(20):
    vi = int(input("digite um valor inteiro"))
    if vi > 0:
        pos+=vi
    else:
        neg+=1
print(f"qndt números negativos {neg} soma dos números positivos = {pos}")
