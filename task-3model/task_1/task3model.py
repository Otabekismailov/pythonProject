#
# import datetime
# def convertDate(d):
#     new_date = datetime.datetime.strptime(d[:-1], "%Y-%m-%dT%H:%M:%S")
#     res = str(new_date.date()).replace('-', ' ').replace('.', ' ').split()
#     d = {
#         '01': 'January',
#         '02': 'February',
#         '03': 'March',
#         '04': 'April',
#         '05': 'May',
#         '06': 'June',
#         '07': 'July',
#         '08': 'August',
#         '09': 'September',
#         '10': 'October',
#         '11': 'November',
#         '12': 'December',
#     }
#     for i, v in d.items():
#         if i == res[1]:
#             res[1] = v
#     a = ''
#     for i in res:
#         a += i + ' '
#     return a
#
#
# # print(convertDate("1961-05-31T00:00:00Z"))
#
# import csv
#
# l = []
#
# with open('../pythonProject/P10-test-project/csv_files/Department_Information.csv', 'r') as f:
#     f.readline()
#     data = csv.reader(f)
#     for i in data:
#         l.append({'Department_ID': i[0],
#                   'Department_Name': i[1],
#                   'DOE': convertDate(i[2])
#                   }
#                  )
#
# yechimtask1 = []
#
#
# with open('../pythonProject/P10-test-project/csv_files/Employee_Information.csv', 'r') as f:
#     f.readline()
#     data = csv.reader(f)
#     for i in data:
#
#         d = {'Employee ID': i[0],
#              'DOB': convertDate(i[1]),
#              'DOJ': convertDate(i[2]),
#              'Department_Name': ""
#              }
#         for j in l:
#             if j['Department_ID'] == i[3]:
#                 d['Department_Name']+=j['Department_Name']
#         yechimtask1.append(d)
# satr = ['Employee ID', 'DOB', 'DOJ', 'Department_Name']
# with open('3model.csv', 'w', newline="\n") as f:
#     writer = csv.DictWriter(f, fieldnames=satr)
#     writer.writeheader()
#     writer.writerows(yechimtask1)

# '''
# Birinchi task uchinchi model
#
# Employee ID,DOB,DOJ,Department_Name
# IU196557,1983 February 23,2009 October 31,Civil Engineering
# IU449901,1985 September 02,2009 June 07,Energy Science and Engineering
# IU206427,1971 July 30,2008 May 09,Aerospace Engineering
# '''

# #
# import csv
# # import os
# #
# # # os.mkdir('Instagram accounts')
# # #
# a = []
# l = []
# with open('../pythonProject/P10-test-project/csv_files/List of most-followed Instagram accounts.csv', 'r') as f:
#     f.readline()
#     data = csv.reader(f)
#     for i in data:
#         b = {
#             'UnitedStatesaccounts': i[6],
#             'anomus': i[0],
#             'Rank': i[1],
#             'Username': i[2],
#             'Owner': i[3],
#             "Followers(millions)[2]": i[4],
#             "Profession/Activity": i[5]
#
#         }
#         a.append({'United States accounts': i[6]})
#         l.append(b)
# s = []
# for i in a:
#     for j in l:
#         if i['United States accounts'] == j['UnitedStatesaccounts']:
#             obj = {
#                 'UnitedStatesaccounts': {
#                     'United': i.values()
#                 },
#                 'anomus': j['anomus'],
#                 'Rank': j['Rank'],
#                 'Username': j['Username'],
#                 'Owner': j['Owner'],
#                 "Followers(millions)[2]": j["Followers(millions)[2]"],
#                 "Profession/Activity": j["Profession/Activity"]
#             }
#             s.append(obj)
# print(*s)

# satr = ['Employee , 'DOB', 'DOJ', 'Department_Name']
# with open('United_States_accounts.csv', 'w', newline="\n") as f:
#     writer = csv.DictWriter(f, fieldnames=satr)
#     writer.writeheader()
#     writer.writerows(s)

