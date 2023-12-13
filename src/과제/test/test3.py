import random

lot = []

while True:
    r = random.randint(1,45)
    if r not in lot:
        lot.append(r)
        if len(lot) == 6:
            break
print(sorted(lot))