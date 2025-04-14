import streamlit as st
from mat import *
from diskcache import Cache

cache=Cache("cache")
st.set_page_config(page_title="pokemon", 
	page_icon="""https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/25.gif""",
	layout="wide",
	initial_sidebar_state="collapsed",  
	menu_items=None)

st.title("pokedex")


for x in range(0,len(array_matrix)):

	col=[]
	y=len(col)

	col=st.columns(5,border=True)


	for i in col:
		if cache[array_matrix[x][y]][7] == None:
			check=(cache[array_matrix[x][y]][7]== None and cache[array_matrix[x][y]][8]== None
				and cache[array_matrix[x][y]][6]== None and cache[array_matrix[x][y]][5]== None)
			if check:
				i.image('https://dummyimage.com/475x475/141723/e600ff.png&text=unavailable')
			else:
				i.image(cache[array_matrix[x][y]][6])

		else:
			i.image(cache[array_matrix[x][y]][7])
		i.text(f"#id{cache[array_matrix[x][y]][0]}",help=f"{x}x{y}")
		i.text(f"{cache[array_matrix[x][y]][1]}")
		i.text(f"Type:-{cache[array_matrix[x][y]][4]}")
		i.text(f"height:-{cache[array_matrix[x][y]][2]} decimetres")
		i.text(f"weight:-{cache[array_matrix[x][y]][3]} hectograms")
			
		if array_matrix[x][y]==10277:
			# st.toast(f"{x}x{y}")
			break
		y+=1

