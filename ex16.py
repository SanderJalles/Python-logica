senha = 'jales'
t1 = 1
acesso = input("Digite a senha")
while acesso!=senha:
    t1 = t1+1
    print("BARRADO")
    pin= input()
    print(t1)
    if t1>2 and acesso!=pin:
        print("BARRADO DENOVO")
    if t1>3 and acesso!=pin:
        print("BARRADO TOTALMENTE")
        break
    else:
        print("liberado")
