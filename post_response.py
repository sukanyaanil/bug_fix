import requests

url='https://jsonplaceholder.typicode.com'

def data(url):
    response=requests.get(url+'/posts')
    return response.json()
user=data(url)
print(user)
#
def single_data(url,object):
    response=requests.post(url+'/posts')
    return response.json()
single_user=single_data(url,user)
print(single_user)

def comment_data(url):
    response=requests.delete(url+'/posts')
    return response.json()
get_data=comment_data(url)
print(get_data)

def data_details(url,object):
    response=requests.put(url+'/posts',)
    return response.json()
put=data_details(url,user)
print(put)












# import requests
# def single_data(obj):
#     for i in obj:
#         print(i["id"])
#         # print(i,obj[1])
#         print(i["body"])
#     return obj
#
# obj=[{
#     "userId": 1,
#     "id": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
#   },
#   {
#     "userId": 1,
#     "id": 2,
#     "title": "qui est esse",
#     "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
#   },
#   {
#     "userId": 1,
#     "id": 3,
#     "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
#     "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
#   }]
# print(single_data(obj))