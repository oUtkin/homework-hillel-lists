# Завдання 5:
# Запросити користувача 5 чисел і записати їх до списку A
# Записати всі числа зі списку A які більше 5 до списку C

A = []
C = []
for i in range(1, 6):
    A.append(int(input(f'Enter #{i} number: ')))

for j in A:
    C.append(j) if j > 5 else None
print(C)
