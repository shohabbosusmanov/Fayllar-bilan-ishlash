dc = {"Ism": "Ali", "Familiya": "Valiyev", "Yosh": 28}

k = input("kalitni kiriting:\n")

try:
    qiymat = dc[k]
    print(qiymat)
except KeyError:
    print(f"{k} nomli kalit topilmadi")
