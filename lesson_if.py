#Попросить пользователя ввести возраст при помощи input и положить результат в переменную
#Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
#Вызвать функцию, передав ей возраст пользователя, и положить результат работы функции в переменную
#Вывести содержимое переменной на экран

age_user = input('Введите ваш возраст:')
age1 = int(age_user)

if 0< age1 <= 6:
    print('Детский сад!')
elif 6 < age1 < 16:
    print('Школа')
elif 16 < age1 < 22 or 23:
    print('ВУЗ')
else :
    print('Работа')

