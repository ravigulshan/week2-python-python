# more about get, two same key in dictionaries
user = {'name': 'SUNNY','age':19, 'age':20}
print(user.get('name'))
print(user.get('fav','not found!'))
print(user)