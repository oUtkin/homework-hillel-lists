# Завдання 3:
# Запросити користувача 10 чисел і записати їх до списку A
# Запросити у користувача число N
# Вивести користувачу скільки у списку A повторюється число N

new_list = []
for i in range(1, 11):
    new_list.append(int(input(f'Enter #{i} number: ')))
print(new_list)

N = int(input('Enter N: '))

print(f'{N} has founded {new_list.count(N)} times')
