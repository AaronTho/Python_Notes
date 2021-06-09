# The strip method removes whitespace or a specific element.

url = 'https://google.com'

# print(url.strip('https://'))

url = (url.lstrip('https://'))
url = (url.rstrip('.com'))
url = url.capitalize()

print(url)
