"""
 Винни-Пух попросил вас посмотреть, есть ли в стихах ритм. Поскольку разобраться в кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  
    """


word = input("Введите фразу: ")
vowel = ['a', 'o', 'э', 'e', 'и', 'ы', 'ё', 'ю', 'я']
str = str.split()
result = list()
for item in str:
    i = 0
    for letter in item:
        if letter in vowel:
            i += 1
    result.append(i)
if len(set(result)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')