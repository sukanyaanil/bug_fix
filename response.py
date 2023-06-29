import requests
from requests import status_codes
data=[]
j=0
x=requests.get('https://jsonplaceholder.typicode.com/posts')
print(type(x.status_code))
# print(x.url)
# print(x.headers)
# print(x.encoding)
# print(x.elapsed)
# print(x.close())
# print(x.content)
# print(x.cookies)
# print(x.history)
# print(x.is_redirect)
# print(x.is_permanent_redirect)
print(x.json())
print(x.text)
# print(x.request)
# print(x.reason)
print(x.links)
if x.status_code == 200:
    print('Success!')
    for i in x.json():
        data.append(i)
elif x.status_code == 404:
    print('Not Found.')
else:
    print("hi")
print(type(data))
for value in data:
    print(value["id"])

# print(x.status_code)
# print(x.content)