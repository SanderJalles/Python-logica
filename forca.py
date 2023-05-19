import random

palavras = ["Malenia", "Maliketh", "Godrick", "Radahn", "Radagon", "Rennala", "Mohg", "Rykard", "Margit", "Alecto",
"Godfrey"]

palavra = random.choice(palavras)
tentativas = 0
cc = len(palavra)
chance = 5

letra_escolhida = []

palavra_atual = ["_"] * len(palavra)

print("Bem vindo as terras intermedias")
print("Seu objetivo é adivinhar os respectivos semideuses das terras intermedias")
print("Tente por letra por letra e caso a letra esteja presente em seus respectivos nomes, sera printado na tela.")
print("O usuario tera apenas 5 chances para acertar caso erre todas a praga da morte ira lhe levar")


while tentativas < chance:
    opcao = int(input("Escolha 1 para chutar e 2 para continuar "))

    if opcao == 1:
        chute = input("Digite o nome que voce acha que é")
        if chute == palavra:
            print("Voce acertou")
            break
        else:
            print("vacilou,perdeu tudo")
            break
    else:
        letra = input("\nEscolha uma letra ! ").lower()

        while letra in letra_escolhida:
            print("Letra ja escolhida, tente novamente !")
            letra = input("\nEscolha uma letra !")
        letra_escolhida.append(letra)

        if letra in palavra.lower():
            print("A letra esta presente")
            for i in range(len(palavra)):
                if letra == palavra[i].lower():
                    palavra_atual[i] = letra
                    cc -= 1
        else:
            print("Cuidado maculado voce perdeu 1 tentativa")
            tentativas = tentativas + 1


        print("Restam ", chance - tentativas, "tentativas")
        print("Estado atual do nome")
        print(palavra_atual)

        if cc == 0:
            break

        print("\nAs lentras que foram tentadas são:")
        print(", ".join(letra_escolhida))

if tentativas == chance:
    print("Voce morreu")

else:
    print("Parabens maculado voce passou no teste")


print("A palavra era", palavra)

