
year_birth = 1799  # год рождения Пушкина

year_birth_input = 0

while year_birth_input != year_birth:
    year_birth_input: str = input("Введите год рождения Пушкина: ")  # полученное значение года Рождения Пушкина
    if not year_birth_input.isdigit():
        print('Введите год рождения цифрами')
    # Проверка условия if
    else:
        year_birth_input = int(year_birth_input)
    day_birth = 6
    if year_birth == year_birth_input:
        day_birth_input: str = input("Введите день рождения Пушкина: ")
        if int(day_birth_input) == day_birth:
            print('верно')
        else:
            print('Неверный день рождения')

    else:
        print('Неверный год')