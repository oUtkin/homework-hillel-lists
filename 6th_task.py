# Завдання 6:
# Запросити у користувача число N
# Запросити користувача N цілих чисел і записати їх до списку A
# Знайти в ньому мінімальну та максимальну кількість за допомогою циклу
# (заборонено використовувати функцію min, max, sorted, sort). Вивести ці числа.

N = int(input('Enter N: '))
new_list = []
for i in range(1, N + 1):
    new_list.append(int(input(f'Enter #{i} number: ')))

min_number = new_list[0]
max_number = new_list[0]
for i in new_list:
    if i > max_number:
        max_number = i
    elif i < min_number:
        min_number = i
print(f'Biggest number: {max_number}\nLowest number: {min_number}')
