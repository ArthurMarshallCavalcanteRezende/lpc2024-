print("Número por extenso")

num = int(input("Insira um número de 1-99: "))

algarismos = [
    "", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
    "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"
]

decimais = [
    "", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"
]

if num < 100:
    variavel = str(num)

    if 0 < num < 20:
        print(f"{num} em extenso é: {algarismos[num]}")

    elif variavel[1] == "0":
        segundo = algarismos[int(variavel[1])]
        primeiro = decimais[int(variavel[0])]
        print(f"{num} em extenso é: {primeiro}")
    else:
        segundo = algarismos[int(variavel[1])]
        primeiro = decimais[int(variavel[0])]
        print(f"{num} em extenso é: {primeiro} e {segundo}")
