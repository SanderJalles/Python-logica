contador = 0
fora = 0
for x in range(10):
    num = int(input("Digite os valores"))
    if num >= 10 and num<=20:contador +=1
    else:
        fora+=1

print(contador, fora)