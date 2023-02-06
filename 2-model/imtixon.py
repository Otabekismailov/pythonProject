# # n = int(input())
# # a = 1
# #
# # for i in range(n):
# #     b = []
# #     for j in range(n):
# #         b.append(a)
# #         a += 1
# #     print(b)
# # a = 1
# # for i in range(n):
# #     b = []
# #     for j in range(n):
# #         if n // 2 == j or i == 0:
# #             b.append(a)
# #
# #         else:
# #             b.append(' ')
# #         a += 1
# #     print(*b)
#
import http
import yaml
import csv
import json

d = {}
l = []
with open('regions.csv', 'r') as file:
    file.readline()
    data = csv.reader(file)
    for i in data:
        d.update({i[0]: i[1]})
print(d)
file = open(f'viloyat.json', 'w')
json.dump(d, file, indent=2)
with open('districts.csv', 'r') as file:
    file.readline()
    data = csv.reader(file)
    for i in data:
        l.append({
            'id': i[0],
            'name': i[1],
            'region': d[i[2]]})
fayl = open('id.json', 'w')
json.dump(l, fayl, indent=2)
fayl.close()
tumanlar = []
header = ['data', 'object', 'districts', 'fields', "region", 'pk']
for _, name in d.items():
    obj = {
        'data': {
            'object': 'apps.adverts.region',
            'districts': ""
        },
        'fields': {
            "region": name,
            'pk': int(_)
        }
    }

    for item in l:
        if item["region"] == name:
            obj["data"]["districts"] +=(item["name"])
    tumanlar.append(obj)
with open('Tumanlar.json', 'w') as f:
    json.dump(tumanlar, f, indent=2)

#
#
#
# with open(csv_file_path, "a", newline="\n") as f:
#     # laptops_data[0].update({"name": f"\n{laptops_data[0].get('name')}"})
#     csv_writer = csv.DictWriter(f, header)
#     csv_writer.writerows(laptops_data)
