# usando o laço for
for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print("Usando FOR:", andar)

# Usando o laço while
andar = 20
while andar >= 1:
    if andar == 13:
        andar -= 1 
        continue
    print("Usando WHILE:", andar)
    andar -= 1

# Usando o Laço Do-While
andar = 20
while True:
    if andar == 13:
        andar -= 1
        continue
    print("Usando DO-WHILE:", andar)
    andar -= 1
    if andar < 1:
        break
