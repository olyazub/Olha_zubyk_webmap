
import folium
from Olha_Zubyk_locations import films_year, find_location, read_file
import random

def user_interaction():
    """
    None -> (list
    Gets year and number of films from a user
    and returns a list of unique random films
    """
    try:
        year = int(input("Please enter a year: "))
        films = films_year(read_file("locations.list"), year)
        print('In this year, {} films were produced'.format(str(len(films))))
        num = int(input("How many (maximum) films do you want to see? "))
        films1 = []
        while len(films1) < num:
            index = random.randint(0, len(films)-1)
            if films[index] not in films1:
                films1.append(films[index])
            else:
                continue
        return films1
    except ValueError:
        print("Both answers should be a number")


maps = folium.Map(location=[49.84441000000004, 24.02543000000003],
           tiles='Stamen Toner',
           zoom_start=3)

fg = folium.FeatureGroup(name="films")


for el in user_interaction():
    fg.add_child(folium.Marker(location=find_location(el[-1]),
                                 popup=str(el[0]),
                                 icon=folium.Icon(color='red',icon='info-sign')))

maps.add_child(fg)


la = folium.FeatureGroup(name="population")


la.add_child(folium.GeoJson(data = open ('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': '#D7DF01'
        if x['properties']['POP2005'] < 10000000
        else '#A5DF00' if 10000000 <= x['properties']['POP2005'] < 20000000
        else '#DBA901'}))

maps.add_child(la)

maps.add_child(folium.LayerControl())

maps.save("Olha_zubyk_map.html")



