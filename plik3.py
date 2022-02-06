import csv

# with open('titanic.csv') as file:
#     data = csv.reader(file)
#     for r in data:
#         print(r)

# with open('titanic.csv') as file:
#     data = csv.DictReader(file)
#     struct = [row for row in data]
#     print(struct[1]['Name'])

with open('titanic.csv', newline='') as file:
    dialect = csv.Sniffer().sniff(file.read())
    print(file)