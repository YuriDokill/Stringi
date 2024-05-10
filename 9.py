user = input('Введи строку:')
pstring = input('Введи подстроку для проверки:')
if user.startswith(pstring):
    print('Строка начинается с указанной подстроки')
else:
    print('Строка не начинается с указанной подстроки')