import requests
import folium


def get_coordinates(address):
    """
    Function to retrieve latitude and longitude coordinates for a given address.
    """
    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(geocoding_url)
    data = response.json()
    if data.get("status") == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        print(f"Error: Unable to retrieve coordinates for {address}.")
        return None


def get_country(address):
    """
    Function to retrieve the country for a given address.
    """
    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(geocoding_url)
    data = response.json()
    address_components = data["results"][0]["address_components"]
    country = next((component["long_name"] for component in address_components if "country" in component["types"]), None)

    return country


def get_visited_places():
    """
    Function to retrieve a list of places the user wants to visit.
    """
    visited_places = [
        "Warsaw", "Wroclaw", "Berlin", "Bratislava", "Prague", "Kittilä", "Stockholm", "Copenhagen", "Malmo",
        "Reykjavik", "Oslo", "Brussels", "Lille", "London", "Lisbon", "Porto", "Funchal", "Barcelona", "Alicante",
        "Mallorca", "Valletta", "Tunis", "Rome", "Vatican City", "Florence", "Pisa", "Venice", "Davos",
        "Vaduz", "Bregenz", "Ljubljana", "Zagreb", "Budapest", "Belgrade", "Skopje", "Tirana", "Podgorica", "Prishtina",
        "Thessaloniki", "Sofia", "Chania", "Bodrum", "Nicosia", "Paphos", "Larnaca", "Kutaisi", "Batumi", "Abu Dhabi",
        "Dubai", "Muscat", "Port Louis", "Tiwi"
    ]

    # while True:
    #     place = input("Enter a place you have visited (or 'done' to finish): ")
    #     if place == "done":
    #         break
    #     else:
    #         visited_places.append(place)

    return visited_places


def get_user_map():
    """
    Function to retrieve a map of visited places.
    """
    visited_places = get_visited_places()
    map_center = get_coordinates(visited_places[0])

    my_map = folium.Map(location=map_center, zoom_start=10)

    country_flag_icons = {
        "Albania": "flags/albania.png",
        "Austria": "flags/austria.png",
        "Belgium": "flags/belgium.png",
        "Bulgaria": "flags/bulgaria.png",
        "Croatia": "flags/croatia.png",
        "Cyprus": "flags/cyprus.png",
        "Czechia": "flags/czech-republic.png",
        "Denmark": "flags/denmark.png",
        "Finland": "flags/finland.png",
        "France": "flags/france.png",
        "Georgia": "flags/georgia.png",
        "Germany": "flags/germany.png",
        "Greece": "flags/greece.png",
        "Hungary": "flags/hungary.png",
        "Iceland": "flags/iceland.png",
        "Italy": "flags/italy.png",
        "Kosovo": "flags/kosovo.png",
        "Liechtenstein": "flags/liechtenstein.png",
        "Malta": "flags/malta.png",
        "Mauritius": "flags/mauritius.png",
        "Montenegro": "flags/montenegro.png",
        "Norway": "flags/norway.png",
        "Oman": "flags/oman.png",
        "Poland": "flags/poland.png",
        "Portugal": "flags/portugal.png",
        "North Macedonia": "flags/republic-of-macedonia.png",
        "Serbia": "flags/serbia.png",
        "Slovakia": "flags/slovakia.png",
        "Slovenia": "flags/slovenia.png",
        "Spain": "flags/spain.png",
        "Sweden": "flags/sweden.png",
        "Switzerland": "flags/switzerland.png",
        "Tunisia": "flags/tunisia.png",
        "Turkey": "flags/turkey.png",
        "United Arab Emirates": "flags/united-arab-emirates.png",
        "United Kingdom": "flags/united-kingdom.png",
        "Vatican City": "flags/vatican-city.png",
    }

    for place in visited_places:
        place_coordinates = get_coordinates(place)
        country = get_country(place)
        if country in country_flag_icons:
            icon_path = country_flag_icons[country]
            folium.Marker(location=place_coordinates, popup=place,
                          icon=folium.CustomIcon(icon_path, icon_size=(16, 16))).add_to(my_map)
        else:
            folium.Marker(location=place_coordinates, popup=place,
                          icon=folium.Icon(color="green")).add_to(my_map)

    my_map.save("custom_map.html")
    print("Map saved as custom_map.html")


# Read the API key from a file
api_file = open("api-key.txt", "r")
api_key = api_file.read().strip()
api_file.close()

get_user_map()

