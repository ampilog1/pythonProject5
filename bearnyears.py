# Год рождения Пушкина
year_birth = 1799  # год рождения Пушкина
year_birth_input: str = input("Введите год рождения Пушкина: ")  # полученное значение года Рождения Пушкина
# Проверка условия if
if year_birth_input.isdigit():
    year_birth_input = int(year_birth_input)
else:
    print('Введите год рождения цифрами')

if year_birth == year_birth_input:
    print('Верно')
else:
    print('Неверно')
