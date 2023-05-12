n1 = float(input("Digite a primeira nota"))
while n1 < 0 or n1 > 10:
    print("Nota invalida digite de 0 a 10")
    n1 = float(input("Digite sua primeira nota"))

n2 = float(input("Digite sua segunda nota"))
while n2 < 0 or n2 > 10:
    print("Nota invalida digite de 0 a 10")
    n2 = float(input("Digite a segunda nota"))
media = (n1 + n2)/2
print(media)



pergunta = input("Deseja continuar ?")
while pergunta == "sim":
    n1 = float(input("Digite a primeira nota"))

    while n1 < 0 or n1 > 10:
        print("Nota invalida digite de 0 a 10")
        n1 = float(input("Digite sua primeira nota"))

    n2 = float(input("Digite sua segunda nota"))
    while n2 < 0 or n2 > 10:
        print("Nota invalida digite de 0 a 10")
        n2 = float(input("Digite a segunda nota"))
    media = (n1 + n2) / 2
    print(media)
    pergunta = input("Deseja continuar ?")
