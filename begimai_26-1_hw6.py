import re

while True:
    try:
        menu = int(input(f'Выберите опцию из меню:\n'
                         f'1. Считать имена и фамилии.\n'
                         f'2. Считать все емайлы.\n'
                         f'3. Считать названия файлов.\n'
                         f'4. Считать цвета.\n'
                         f'5. Выход.\n'
                         f'Ваш выбор: '))

        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            if menu == 1:
                fullName = re.findall(r"([A-Z][a-zA-Z-]*)\s(([A-Za-z]+\s([A-Z][a-zA-z'-]*))|([A-Z][a-zA-z'-]*))", content)

                with open('names.txt', 'w') as file:
                    file.write(f'{len(fullName)}' + f' {fullName}')
                    print(f'Вы выбрали считать все имена и фамилии. Данные в {len(fullName)} строк '
                        f'сохранились в файле под названием names.txt.')
            elif menu == 2:
                emails = re.findall(r'([a-z0-9]*@[a-z0-9-]*\.[a-z]*\.[a-z]*)|([a-z0-9]*@[a-z0-9-]*\.[a-z]*)', content)
                with open('emails.txt', 'w') as file:
                    file.write(f'{len(emails)}' + f' {emails}')
                    print(f'Вы выбрали считать все емайлы. Данные в {len(emails)} строк '
                          f'сохранились в файле под названием emails.txt.')
            elif menu == 3:
                files = re.findall(r'[A-Z][A-Za-z]*\.[a-z0-9]{3,4}', content)
                with open('files.txt', 'w') as file:
                    file.write(f'{len(files)}' + f' {files}')
                    print(f'Вы выбрали считать все названия файлов. Данные в {len(files)} строк '
                          f'сохранились в файле под названием files.txt')
            elif menu == 4:
                colors = re.findall(r'#[a-z0-9]{1,6}', content)
                with open('colors.txt', 'w') as file:
                    file.write(f'{len(colors)}' + f' {colors}')
                    print(f'Вы выбрали считать все цвета. Данные в {len(colors)} строк '
                          f'сохранились в файле под названием colors.txt')
            elif menu == 5:
                print('Выход...')
                break
            else:
                print('Вы можете выбирать только из предложенного в меню!')

    except:
        print('Только цифры от 1 до 5!!!')