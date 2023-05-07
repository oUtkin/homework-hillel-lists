# Завдання 4:
# Запросити у користувача число N
# Запросити користувача N чисел і записати їх до списку A
# Вивести список у зворотній послідовності

N = int(input('Enter N: '))
new_list = []
for i in range(1, N + 1):
    new_list.append(int(input(f'Enter #{i} number: ')))
new_list.reverse()
print(new_list)
