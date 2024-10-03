matn = input("matn kiriting:\n")

for i in matn:
    if not i.isalpha():
        raise("matnda haflardan boshqa belgilar kiritilgan")

print("matn faqat harflardan iborat")