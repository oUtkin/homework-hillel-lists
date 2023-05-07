# Завдання 1:
# Запросити користувача 5 чисел і записати їх до списку

new_list = []
for i in range(1, 6):
    new_list.append(int(input(f'Enter #{i} number: ')))
print(new_list)
