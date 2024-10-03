with open("masala5.txt", "r") as fl:
    matn = fl.read()

matn = list(map(lambda s: s[::-1], matn.split()))

with open("masala5_1.txt", "w") as f:
    for i in matn:
        f.write(i + " ")