op = '5'
while  op == '5':
    n1 = float(input("Digite o primeiro numero"))
    n2 = float(input("Digite o segundo numero"))
    op = input("Selecione a operation")
    if op == '1':
        resultado = n1 + n2
        print(resultado)
    if op == '2':
        resultado = n1 - n2
        print(resultado)
    if op == '3':
        resultado = n1 * n2
        print(resultado)
    if op == '4':
        resultado = n1 / n2
        print(resultado)
if op == '6':
    print("encerrado")