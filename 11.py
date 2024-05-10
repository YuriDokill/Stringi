user = input('Введи строку:')
pstring = input('Введи строку для поиска:')
index = user.find(pstring)
if index != -1:
    print(f'Подстрока найдена в индексе {index}')
else:
    print('Подстрока не найдена (')
