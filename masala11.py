fayl = input("fayl nomini kiriting:\n")

try:
    with open(fayl, "r") as f:
        matn = f.read()
except FileNotFoundError:
    print(f"{fayl} nomli fayl topilmadi")
