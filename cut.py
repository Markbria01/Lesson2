#Задание 1
#Перепишите функцию hello_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" и завершала работу при помощи оператора break

def hello_user():
    try:
        user_say = input('Как дела: ')
        while user_say != 'Хорошо':
            user_say = input('Как дела: ')
            return()
        print(f'Отлично что {user_say}!')
    except KeyboardInterrupt:
        print('By!')
    
hello_user()