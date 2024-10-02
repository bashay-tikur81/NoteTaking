
from city_function import city

def test_city_country():
    ''' Does Santiago, chile words'''
    city_name = city("santiago", "chile")
    assert city_name == "Santiago, Chile"

def test_city_country_population():
    city_population = city("santiago", "chile", 30000)
    assert city_population == "Santiago, Chile - Population 30000"
    
