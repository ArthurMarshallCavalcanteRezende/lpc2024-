import random


def roll_dice(a):
    a += random.randint(1, 6)
    return a


print("Role os dados!")
vetor = []
for i in range(10):
    valor = 0
    vetor.append(roll_dice(valor))
print(vetor)

for j in range(1, 6):
    repetidos = vetor.count(j)
    if repetidos == 0:
        print(f"O valor {j} não consta no histórico de rolagens.")
    else:
        print(f"O valor {j} repetiu {repetidos} vezes.")
