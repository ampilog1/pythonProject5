year_birth = 1799  # год рождения Пушкина
year_birth_input: str = input("Введите год рождения Пушкина: ")  # полученное значение года Рождения Пушкина

# Проверка условия if
if year_birth_input.isdigit():
    year_birth_input = int(year_birth_input)
else:
    print('Введите год рождения цифрами')
day_birth = 6
if year_birth == year_birth_input:
    day_birth_input: str = input("Введите день рождения Пушкина: ")
    if int(day_birth_input) == day_birth:
        print('верно')
    else:
        print('Неверный день рождения')

else:
    print('Неверный год')