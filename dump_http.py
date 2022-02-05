import requests

url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
# print(response.text)
# print(response)
print(response.headers)