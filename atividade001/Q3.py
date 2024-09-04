def verifica_formato(cpf):
    if cpf[3] != "." or cpf[7] != ".":
        return print(f"CPF inválido, falta de '.'")
    if cpf[11] != "-":
        return print(f"CPF inválido, falta de '-'")
    elif len(cpf) > 14:
        return print("CPF inválido por ultrapassagem do número de caracteres apropriado.")
    else:
        return print("Formatação correta.")


def int_transformer(cpf, nine_or_ele):
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    cpf_int = [int(char) for char in cpf]
    cpf_um = []
    contador = 0
    for i in cpf_int:
        if contador < 9 and nine_or_ele == "9":
            cpf_um.append(i)
            contador += 1
        if contador < 11 and nine_or_ele == "11":
            cpf_um.append(i)
        else:
            continue
    return cpf_um


def value_one(cpf_int):
    mult = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    resul = [a * b for a, b in zip(mult, cpf_int)]
    soma = sum(resul)
    resto = soma % 11
    if resto < 2:
        digito_um = 0
        cpf_int.append(digito_um)
        return cpf_int
    else:
        digito_um = 11 - resto
        cpf_int.append(digito_um)
        return cpf_int


def value_two(cpf_final):
    mult_two = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    resul_final = [a * b for a, b in zip(mult_two, cpf_final)]
    soma_final = sum(resul_final)
    resto_final = soma_final % 11
    if resto_final < 2:
        digito_dois = 0
        cpf_final.append(digito_dois)
        return cpf_final
    else:
        digito_dois = 11 - resto_final
        cpf_final.append(digito_dois)
        return cpf_final


print("Siga o seguinte formato: xxx.xxx.xxx-xx")
informa_cpf = str(input("Informe o seu CPF: "))
nine = "9"
eleven = "11"
verifica_formato(informa_cpf)
cpf_validation = int_transformer(informa_cpf, nine)
cpf_original = int_transformer(informa_cpf, eleven)
join_digit_one = value_one(cpf_validation)
final_validation = value_two(join_digit_one)

if final_validation == cpf_original:
    print("CPF valido, os dois últimos digitos estão corretos!")
