from datetime import datetime

k = input('Quyidagi formatda ("2024-09-30 14:45:12") sana va vaqtni kiriting:\n')
dk = datetime.strptime(k, "%Y-%m-%d %H:%M:%S")
s = datetime.strftime(dk, "%d/%B/%Y, soat %I:%M:%S %p")
print(s)
