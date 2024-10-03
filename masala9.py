import json

with open("masala9.json", "r") as f:
    dc = json.load(f)

print("Ma'lumotlarni yosh bo'yicha filtrlash: yosh > 20")

for i in dc["Malumotlar"]:
    if i["Yosh"] > 20:
        print(i)