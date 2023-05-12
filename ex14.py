soma = 0
i = 1
alunos = int(input("Digite a quantidade de alunos"))
while  i <= alunos:
    num = float(input("Digite as notas"))
    soma += num
    i+=1
    media=soma/alunos
print("A media total é", media)