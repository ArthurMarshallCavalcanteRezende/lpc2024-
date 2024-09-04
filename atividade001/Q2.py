print("-- Identificador de palíndromo --")
informa_user = input("Insira uma palavra ou frase: ")

separador = ""
entrada = separador.join(informa_user.split())

# Esta condicional compara a primeira variável com sua inversa (::-1)
if entrada == entrada[::-1]:
    print(f"\n{informa_user} é um palíndromo.")
    print(f"Original: {informa_user}")
    print(f"Inverso {informa_user[::-1]}")
else:
    print(f"{informa_user} não é um palíndromo")
