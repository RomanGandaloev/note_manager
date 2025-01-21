titles = list()
while True:
    title = input(str('Введите заголовок (для завершения введите стоп или нажмите enter): '))
    if title == str('стоп') or title == str('Стоп') or title == str(''):
        break
    else:
        titles.append(title)
print('Ваши заголовки: ')
for titles in titles:
    print('-',titles)