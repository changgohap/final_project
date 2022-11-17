import requests
import json
import csv
import pandas as pd
from pprint import pprint

URL = 'https://api.themoviedb.org/3/discover/movie?api_key=7096edc06c7259581fd66a5c5483a306&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1 &with_watch_monetization_types=flatrate'
FILE = requests.get(URL).json()

FILE = FILE['results']
print(type(FILE))
# pprint(FILE)