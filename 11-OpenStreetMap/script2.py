import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()], zoom_start=4, tiles='Stamen Terrain')

def color(elev):
    minimum=int(min(df['ELEV']))
    step=int((max(df['ELEV']) - min(df['ELEV']))/3)

    if elev in range(minimum, minimum+step):
        col = 'green'
    elif elev in range(minimum+step, minimum+step*2):
        col='orange'
    else:
        col='red'
    return col

fg=folium.FeatureGroup(name='Volcano Locations')

for lat, lon, name, elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):

    #map.simple_marker(location=[lat, lon], popup=name, marker_color=color(elev))
    map.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color(elev))))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('world_population.json'),
                             name='World Population',
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save(outfile='test4.html')