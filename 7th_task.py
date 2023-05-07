# Завдання 7:
# Користувач вводить текст потрібно вивести кількість цифр у цьому тексті
# Приклад:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Кількість цифр: 7

text = input('Enter your text: ')
new_list = []

for i in text:
    if i.isdigit():
        new_list.append(i)
print(f'{len(new_list)} digits founded')
