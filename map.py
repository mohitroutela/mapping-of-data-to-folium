import folium
import pandas
data=pandas.read_csv("final1.csv")
lat=list(data["Latitude"])
lon=list(data["Longitude"])
info=list(data["University"])
rnk=list(data["Rank"])

def get_rank(rank):
	if rank<100:
		return 'red'
	elif 100<=rank<=300:
		return 'orange'
	else:
		return 'blue'
	

map=folium.Map(location=[20.5937, 78.9629],zoom_start=4,tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="my map")

#fg.add_child(folium.Marker(location=[38.2,-99.1],popup="hi this is mohit",icon=folium.Icon(color='green')))
#one way to add more markers
'''
	fg.add_child(folium.Marker(location=[37.2,-98.1],popup="hi this is mohit",icon=folium.Icon(color='green')))
	fg.add_child(folium.Marker(location=[36.2,-95.1],popup="hi this is mohit",icon=folium.Icon(color='green')))
'''
# another way to add more markers
for lt,ln,inf,rk in zip(lat,lon,info,rnk):
	# for circular marker --fg.add_child(folium.CircleMarker(location=[lt,ln],radius=10,popup=folium.Popup(str(inf),parse_html=True,fill_color=get_rank(rk),color='grey',fill_opacity=0.7))
	# 
	fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(inf),parse_html=True),icon=folium.Icon(color=get_rank(rk))))


map.add_child(fg)
map.save("map.html")

