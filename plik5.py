import os
from datetime import datetime

stats = os.stat(('wynik1.txt'))
print(stats.st_size)
print(datetime.fromtimestamp(stats.st_mtime))
print(datetime.fromtimestamp(stats.st_atime))