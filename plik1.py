import os

# for root, dirs, files in os.walk('.'):
#     for file in files:
#         print(file)

# for root, dirs, files in os.walk('.'):
#     for file in files:
#         full_path = os.path.join(root,file)
#         print(full_path)

# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if file.endswith('.pdf'):
#             full_path = os.path.join(root, file)
#             print(full_path)
import re

# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if re.search(r'[13579]', file):
#             full_path = os.path.join(root, file)
#             print(full_path)

for root, dirs, files in os.walk('.'):
    print(root, dirs, files)
