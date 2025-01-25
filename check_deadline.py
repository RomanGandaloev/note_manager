from datetime import datetime   # Загружаем встроенную библиотеку datetime

current_date = datetime.now().date()    # Программа показывает текущую дату
print('Текущая дата: ', current_date.strftime('%d-%m-%Y'))      #'%Y-%m-%d'

while True:                             # Запрашиваем у пользователя дату дедлайна
    issue_date = input('\nВведите дату истечения дедлайна заметки в формате дд-мм-гггг, например 25-12-2025: ')
    try:                                # Преобразуем введённую строку в объект datetime
        issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
        print('Дата дедлайна успешно введена!\n')
        break
    except ValueError:
        print('Неверный формат даты, попробуйте снова.')

if current_date == issue_date:           # Сравниваем даты
    print('Дедлайн истекает сегодня!')
elif current_date < issue_date:
    diff = issue_date - current_date
    print('До дедлайна осталось', diff.days, 'дней.')
else:
    diff = issue_date - current_date
    print('Дедлайн просрочен на', (diff.days * -1), 'дней!')