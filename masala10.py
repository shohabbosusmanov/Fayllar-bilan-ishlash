import json

with open("masala10.json", "r") as f:
    dc = json.load(f)

dc = dict(dc)

max_qiymat = float('-inf')
min_qiymat = float('inf')

for i in dc["Malumotlar"]:
    for j in i.values():
        if isinstance(j, int):
            if j > max_qiymat:
                max_qiymat = j
            if j < min_qiymat:
                min_qiymat = j
    
            
            
print(f"fayldagi raqamli malumotlarning eng kattasi {max_qiymat}, eng kichigi {min_qiymat}")