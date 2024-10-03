with open("masala4.txt", "r") as fl:
    matn = fl.read()

ls = list(map(str, matn.split()))
ls.sort(key=lambda c: len(c))

print(f"fayldagi eng uzun so'z: {ls[-1]}\neng qisqa so'z: {ls[0]}")