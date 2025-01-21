status = input('Введите статус заметки: ')
print('Ваш статус заметки: ', status)
print('''Введите новый статус заметки: 
1 - Выполнено
2 - В работе
3 - Отложено''')
status_new = True
while status_new:
    number = input('Введите значение, соответствующее статусу: ')
    if number == str(1) or number == str('Выполнено'):
        number = 'Выполнено'
        status_new = False
    elif number == str(2) or number == str('В работе'):
        number = 'В работе'
        status_new = False
    elif number == str(3) or number == str('Отложено'):
        number = 'Отложено'
        status_new = False
    else:
        print('''Неправильный ввод, повторите ввод
        1 - Выполнено
        2 - В работе
        3 - Отложено''')
print('Новый статус заметки: ', number)