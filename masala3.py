with open("masala3.txt", "r") as fl:
    matn = fl.read()

print(f"fayda {matn.count(" ") + 1} ta so'z bor")