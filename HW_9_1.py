from pprint import pprint
import requests

# url = "https://superheroapi.com/api/2619421814940190/search/Thanos"
# responce = requests.get(url)
# pprint(responce.json())

name = ['Hulk', 'Captain America', 'Thanos']
super_hero = {}
a = 0
clever = None
for i in name:
    url = "https://superheroapi.com/api/2619421814940190/search/" + i
    responce = requests.get(url)
    result = responce.json()['results']
    super_hero[i] = result[0]['powerstats']['intelligence']
    super_hero = {k: int(v) for k, v in super_hero.items()}
   
pprint(super_hero)
pprint(f'Самый умный из супергероев: {max(super_hero, key=super_hero.get)}')


# Второй вариант решения:
# from pprint import pprint
# import requests

# def max_val(d):
#     v = list(d.values())
#     k = list(d.keys())
#     result = k[v.index(max(v))]
#     print(result)
#     return result

# def superhero(names, criterion):
#     super_hero = {}
#     for name in names:
#         url = "https://superheroapi.com/api/2619421814940190/search/" + name
#         responce = requests.get(url)
#         results = responce.json()['results']
#     # super_hero[i] = result[0]['powerstats']['intelligence']
#         if results[0].get('name') == name:
#             super_hero.update({name: results[0]['powerstats']['intelligence']})
#     super_hero = {k: int(v) for k, v in super_hero.items()}
#     pprint(super_hero)
#     hero_name = max_val(super_hero)
#     return hero_name

# superhero(['Hulk', 'Captain America', 'Thanos'], ['intelligence'])