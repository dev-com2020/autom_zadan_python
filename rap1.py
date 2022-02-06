from datetime import datetime

TEMPLATE = '''

Raport na temat gier
----------------

Data: {date}
Liczba gier w które zagrałem w ciągu ostatnich 30 dni: {num_game}
Łączny czas grania w minutach: {total_minutes}
'''

data = {
    'date': datetime.utcnow(),
    'num_game': 3,
    'total_minutes': 376,
}

report = TEMPLATE.format(**data)

FILENAME_TMPL = "{date}_report.txt"
filename = FILENAME_TMPL.format(date=data['date'].strftime('%Y-%m-%d'))
print(filename)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(report)
