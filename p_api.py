import requests as req
import json,threading
from diskcache import Cache
"""
a file to generage pokemon diskcache for fast storage of api father than 
calling it multiple time directly storing the information in the disk 
for fast acces 

"""
cache=Cache("cache")
# dic={}

# @cache.memoize()
def get_data(p_id):
	print()
	global cache
	res=req.get(p_id)
	# print("featching pokemon")
	data=res.json()
	cache.add(data['id'],(data['name'],data['height'],data['weight']))
	cache[data['id']]=(
		data['id'],   
		data['name'],
		data['height'],
		data['weight'],
		data['types'][0]['type']['name'],
		data['sprites']['front_default'],
		data['sprites']['other']['official-artwork']['front_default'],
		data['sprites']['other']['official-artwork']['front_shiny'],
		data['sprites']['front_shiny'])
	# print(
	# 	(data['id'],data['name'],data['height'],
	# 	data['weight'],
	# 	data['types'][0]['type']['name'],
	# 	data['sprites']['front_default'],
	# 	data['sprites']['front_shiny'],
	# 	data['sprites']['other']['official-artwork']['front_default'],
	# 	data['sprites']['other']['official-artwork']['front_shiny'])
	# )
	print(f"adding {p_id} {data['name']}")

# def data_formatter(data):
# 	return 
# res=req.get("https://pokeapi.co/api/v2/pokemon/?limit=13")
# res=req.get("https://pokeapi.co/api/v2/pokemon/?limit=1302")

# data=res.json()
# res2=data['results']
# # print(res2,data['results'][0]['url'])

# threads=[]
# for i in res2:
# 	thread = threading.Thread(target=get_data, args=(i['url'],))
# 	thread.start()
# 	threads.append(thread)

# for thread in threads:
# 	thread.join()
for i in range(10263,10278):
	print(cache[i])
# cache[10145]=(10145, 'mimikyu-totem-busted', 4, 28, 'ghost', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10145.png', None, 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/10145.png', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/778-totem-busted.png')
# print(cache[10145])

# lst_s=sorted(list(cache))
# # print(len(lst_s))
# # print(max(lst_s),min(lst_s))
# matrix=[]
# try:

# 	for i in range(0,len(lst_s),5):
# 		if i>=1300:
# 			# print(i)
# 			# print(lst_s[i],lst_s[i+1],None,None,None)
# 			matrix.append((lst_s[i],lst_s[i+1],None,None,None))

# 		else:
# 			# print(lst_s[i],lst_s[i+1],lst_s[i+2],lst_s[i+3],lst_s[i+4])
# 			matrix.append((lst_s[i],lst_s[i+1],lst_s[i+2],lst_s[i+3],lst_s[i+4]))
# except Exception as e:
# 	print(e)


# print(matrix)




# print(dict(sorted(dic.items())))
# x=get_data()
# print(data_formatter(get_data(1)))
# for i in x:
# 	print(i)
# for i in x:
# 	print(i,x[i],sep=':')
# 	print()