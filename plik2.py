

# with open('wynik1.txt', 'r') as plik:
#     for line in plik:
#         if 'powinien' in line.lower():
#             print(line)


# with open('wynik1.txt', 'rt', encoding='utf-8') as plik:
#     for line in plik:
#         if 'lepsze' in line.lower():
#             print(line)
#             break
from bs4 import UnicodeDammit

with open('wynik1.txt', 'rb') as plik:
    content = plik.read()

sug = UnicodeDammit(content)
print(sug.original_encoding)
print(sug.unicode_markup)
