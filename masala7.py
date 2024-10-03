import json

ism, familiya, yosh = map(str, input("bir qatorda probel bilan ism, familiya va yosh kiriting:\n").split())
dc = {"ism": ism, "familiya": familiya, "yosh": int(yosh)}

with open("masala7.json", "w") as f:
    json.dump(dc, f)
