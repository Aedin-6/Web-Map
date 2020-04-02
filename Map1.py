import folium
import pandas

map = folium.Map(location=[38.75, - 107.04], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Wulkany")

data = pandas.read_csv("volcanoes.txt")
dataLat = list(data["LAT"])
dataLon = list(data["LON"])
elev = list(data["ELEV"])


def color(e):
    if e < 1000:
        return "green"
    elif 1000 <= e < 3000:
        return "orange"
    else:
        return "red"

for lt, ln, el in (zip(dataLat, dataLon, elev)):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup = str(el)+" m", 
    fill_color = color(el), color = "grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Populacja")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding = "utf-8-sig").read(), 
style_function= lambda x: {"fillColor":"green" if x ['properties']['POP2005'] < 10000000 
else "orange" if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")