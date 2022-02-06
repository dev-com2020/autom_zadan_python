from jinja2 import Template
from datetime import datetime

with open('raport.html', encoding='utf-8') as file:
    template = Template(file.read())

context = {
    'date': datetime.now(),
    'games': ['Minecraft', 'Cyberpunk', 'Wiedźmin'],
    'total_minutes': 404,
}
with open('raport_goto2.html', 'w', encoding='utf-8') as file:
    file.write(template.render(context))
