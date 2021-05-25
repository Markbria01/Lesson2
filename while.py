#Напишите функцию hello_user(), которая с помощью функции input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
def hello_user():
  
    user_say = input('Как дела: ')
    while user_say != 'Хорошо':
        user_say = input('Как дела: ')
        return()
    print(f'Отлично что {user_say}!')
hello_user()