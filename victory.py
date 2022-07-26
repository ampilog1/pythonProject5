#  переменные с правильными ответами
year_birth_tolstoy = '1828'  # год рождения Толстой Л.Н.
year_birth_dostoyevskiy = '1821'  # год рождения Достоевский Ф.М.
year_birth_Lermontov = '1814'  # год рождения Лермонтов М.Ю
year_birth_Ahmatova = '1889'  # год рождения Ахматовой А.А.
year_birth_Gumilev = '1886'  # год рождения Гумилева Н.Г.

i = 0  # счетчик правильных ответов
j: int = 0  # счетчик неправильных ответов
beginning = 'да'  # условие начала цикла

while beginning == 'да':
    year_birth_input_tolstoy = input("Введите год рождения Л.Н.Толстого(1828): ")
    if year_birth_input_tolstoy == year_birth_tolstoy:
        i = i + 1
        print('Правильных ответов: ', i)
    else:
        j = j + 1
        print('Ошибок: ', j)

    year_birth_input_dostoyevskiy = input("Введите год рождения Ф.М.Достоевского(1821): ")
    if year_birth_input_dostoyevskiy == year_birth_dostoyevskiy:
        i = i + 1
        print('Правильных ответов: ', i)
    else:
        j = j + 1
        print('Ошибок: ', j)

    year_birth_input_Lermontov = input("Введите год рождения М.Ю.Лермонтов(1814): ")
    if year_birth_input_Lermontov == year_birth_Lermontov:
        i = i + 1
        print('Правильных ответов: ', i)
    else:
        j = j + 1
        print('Ошибок: ', j)
    year_birth_input_Ahmatova = input("Введите год рождения Ахматовой А.А.(1889): ")
    if year_birth_input_Ahmatova == year_birth_Ahmatova:
        i = i + 1
        print('Правильных ответов: ', i)
    else:
        j = j + 1
        print('Ошибок: ', j)
    year_birth_input_Gumilev = input("Введите год рождения Гумилева Н.Г.(1886): ")
    if year_birth_input_Gumilev == year_birth_Gumilev:
        i = i + 1
        print('Правильных ответов: ', i)
    else:
        j = j + 1
        print('Ошибок: ', j)
    quantity_question = 5
    print('Количество правильных ответов: ', i)
    print('Количество ошибок: ', j)
    print('Процент правильных ответов: ', i / quantity_question * 100)
    print('процент ошибок: ', j / quantity_question * 100)

    beginning = input('Если хотите повторить, введите "да": ')
#  привет
