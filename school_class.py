#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

rating_of_schools = [
    {'school_class': '4a', 'scores':[4,5,2,3,5]},
    {'school_class': '4b', 'scores':[3,2,2,5,5]},
    {'school_class': '4c', 'scores':[2,3,3,5,5]} 
]

scores_sum = 0

for score1 in rating_of_schools:
    sum2 = sum(score1['scores']) / len(score1['scores']) 
    print(f'Средняя оценка по школе: {score1["school_class"]} : {sum2}')
    scores_sum += sum2

scores_sum /= len(rating_of_schools)
print(f'Средний бал по школе: {scores_sum}')