import googlemaps
from configparser import ConfigParser

parser = ConfigParser()
parser.read('database.config')


API_KEY = parser.get('database_config', 'api_key')
gmaps = googlemaps.Client(key = API_KEY)
geocode_result = gmaps.geocode('Bharuch')

print(geocode_result)
