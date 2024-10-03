ism, familiya, yosh = map(str, input("bir qatorda probel bilan ism, familiya va yosh kiriting:\n").split())
with open(f"{ism}.txt", "w") as fl:
    fl.write(ism + " " + familiya + " " + yosh)