"""""
country of the world.csv fayldagi raqamlar (,)
bilan tasviryozilgan shu raqamlarni (.)
boshqa csv faylga yozing, bunda (,) bilan ni (.)
uchun writer funktsiyasini decorator orqali ishlating.

"""
import csv


def convert(func):
    def wrapper(file):
        new_rows = []
        rows = func(file)
        for row in rows:
            new_row = [col.replace(',', '.') for col in row]
            new_rows.append(new_row)
        return new_rows

    return wrapper


@convert
def read(file):
    rows = []
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def save_csv(file, rows):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)


input_file = 'countries of the world.csv'
new_file = 'countries of the world_converted.csv'

rows = read(input_file)
save_csv(new_file, rows)
