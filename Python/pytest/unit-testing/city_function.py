
def city(city, country, population=0):
    if population:
        full_city_name = f"{city}, {country} - population {population}"
        return full_city_name.title()
    else:
        full_city_name = f"{city}, {country}"
        return full_city_name.title()
