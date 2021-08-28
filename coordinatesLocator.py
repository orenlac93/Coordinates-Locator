import folium

# input: (Latitude, Longitude) coordinates
# output: create map file of the selected location
#
# the function create html file of the map


def find_map_location(lat, lon):

    print(lat, ',', lon)

    my_map = folium.Map(location=[lat, lon], zoom_start=9)

    folium.Marker([lat, lon], popup=[lat, lon]).add_to(my_map)

    my_map.save("Map.html")


