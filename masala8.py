import json

ism = input("ism kiriting:\n")

with open("masala8.json", "r") as f:
    dc = json.load(f)

dc["ism"] = ism

with open("masala8.json", "w") as f1:
    json.dump(dc, f1)