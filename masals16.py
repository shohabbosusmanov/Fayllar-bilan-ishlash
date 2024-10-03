ls = list(map(int, input("probel bilan sonlar to'plamini kiriting:\n").split()))

for i in range(len(ls) - 1):
    assert ls[i] < ls[i + 1], "sonlar to'plami o'sish tartibida emas"
    
print("sonlar to'plami o'sish tartibida")