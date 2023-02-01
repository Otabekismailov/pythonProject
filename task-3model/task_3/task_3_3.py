'''
planets ushbu fayldagi ma'lumotlardan faqat name olish uchun generator yozing.
planets_gen = gen_func()
print(next(planets_gen))   Mercury
print(next(planets_gen))   Venus
print(next(planets_gen))   Earth
print(next(planets_gen))   Mars
'''''

import csv


def gen(fn):
    with open(fn, 'r') as file:
        data = csv.reader(file)
        for name, dic, mass in data:
            if name == 'name':
                continue
            yield name


res = 'append.csv'
resulat = gen(res)
print(next(resulat))
print(next(resulat))
print(next(resulat))
print(next(resulat))
print(next(resulat))
