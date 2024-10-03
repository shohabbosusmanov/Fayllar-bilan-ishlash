ls = list(map(int, input("probel bilan sonlar to'plamini kiriting:\n").split()))

for i in range(len(ls) - 2):
    assert ls[i] + ls[i + 1] == ls[i + 2], "sonlar to'plami fibonacci ketma-ketligi emas"
    
print("sonlar to'plami fibonacci ketma-ketligi")