import random as r



with open("masala6.txt", "w") as f:
    for i in range(30):
        rand_son = r.randint(1, 100)
        f.write(str(rand_son) + " ")

with open("masala6.txt", "r") as f1:
    sonlar = f1.read()

sonlar = list(map(str, sonlar.split()))

with open("masala6_juft.txt", "w") as f2:
    for i in sonlar:
        if int(i) % 2 == 0:
            f2.write(i + " ")