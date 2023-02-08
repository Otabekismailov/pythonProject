import csv
import os


def student_csv(student):
    with open("student_bot.csv", "a+", newline="\n") as f:
        header = ["caht_id", "full_name"]
        dict_writer = csv.DictWriter(f, header)
        if os.path.getsize("student_bot.csv") == 0:
            dict_writer.writeheader()
        dict_writer.writerow(student)
    print("yukladi")
