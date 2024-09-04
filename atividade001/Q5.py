import random

palavras = []

caminho = input("Insira o caminho do arquivo .txt: ")

with open(caminho, 'r') as arquivo:
    for linha in arquivo:
        palavras.append(linha.strip())

print("Bem vindo ao jogo da forca!")

while True:
    escolha = int(input("Digite 1 para começar ou 0 para encerrar: "))

    if escolha == 0:
        print("Até a próxima.")
        break

    key_word = random.choice(palavras).upper()
    word = []
    print("Que o jogo comece!")
    print("_" * len(key_word))
    for i in range(len(key_word)):
        word.append("_")
    letras = []
    letras_corretas = []
    vida_chances = 6
    index = 0
    conta_tent = 0

    while vida_chances > 0:
        print("Chances restantes: ", vida_chances)
        resposta = input("Digite uma letra: ").upper()
        letras.append(resposta)

        if resposta in key_word:
            letras_corretas.append(resposta)
            for i in range(len(key_word)):
                if resposta == key_word[i]:
                    word[i] = resposta
                    index += 1
            print(f"A palavra é: {word}")

        else:
            conta_tent += 1
            print(f"-> Você errou pela {conta_tent}ª vez. Tente de novo!")
            vida_chances -= 1

        if index == len(key_word):
            print("Parabéns, você acertou a palavra!")
            print(f"A palavra era: {key_word}")
            break

        if vida_chances == 0:
            print("GAME OVER!")
            print(f"A palavra era: {key_word}")
            break

    continuar = input("Deseja continuar? [S/N] ")

    if continuar.upper() == "N":
        print("Até mais!")
        break
    else:
        continue
