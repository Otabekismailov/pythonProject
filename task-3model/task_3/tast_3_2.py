'''
test.txt faylda so'zlar berilgan 

ushbu so'zlardagi har bir harfni 

generator funksiya orqali oling
'''''


def text_generator(text):
    for i in text:
        yield i


lines = 'Hello, Python from P10'
with open('test.txt', 'w') as f:
    for line in lines:
        f.write(line)
a = []
with open('test.txt', 'r') as file:
    line = file.readline()
    for i in line.replace(" ", '').replace(",", ''):
        a.append(i)

new_text = text_generator(a)
print(next(new_text))
print(next(new_text))
print(next(new_text))
