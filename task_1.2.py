#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
#Если строки одинаковые, вернуть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты





def line(str1,str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return '0'
    elif str(str1) == str(str2):
        return '1'
    elif str(str1) > str(str2):
        return '2'
    elif str(str1) != str(str2) or str(str2['learn']): 
        return '3'
    elif str2 =='Learn':
        return '3'

print(line(1,2))
print(line(1,'gif'))
print(line('qw','ew'))
print(line('learn','learn'))