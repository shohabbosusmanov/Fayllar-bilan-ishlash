from datetime import datetime, timedelta

k = input('Quyidagi formatda ("2024-09-30 14:45:12") sana va vaqtni kiriting:\n')
dk = datetime.strptime(k, "%Y-%m-%d %H:%M:%S")
qv = timedelta(days=7, hours=3, minutes=15)
dk += qv
s = datetime.strftime(dk, "%d-%B-%Y %H:%M:%S")
print(s)
