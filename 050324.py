import csv
with open ('FIOandTelephone.csv', 'r', encoding = 'utf-8-sig') as r:
    reader = csv.DictReader(r)
    a = input("Введите ФИО")
    for row in reader:
        if a == row['FIO']:
            print (row['Telephone'])
        else:
            continue

