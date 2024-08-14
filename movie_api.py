import requests
from pprint import pprint

def API_DATA(movie_name):
    API_KEY = '103188594e3dfaadbfece9c681005d49'
    API_BEARER_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMDMxODg1OTRlM2RmYWFkYmZlY2U5YzY4MTAwNWQ0OSIsIm5iZiI6MTcyMzQ1Njg1Ny40MjY2Mywic3ViIjoiNjZiOWRjNDI0YTg1MGExYmI1MWE0ZDgwIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.YvikjBT9VA22-_fGC0YDvVH7xU2tUVC1qR-vKXi8Yw0'

    URL = 'https://api.themoviedb.org/3/search/movie'

    query = {
        'query': movie_name,
        'api_key': API_KEY
    }

    response = requests.get(url=URL, params=query)

    result = response.json()['results']
    return result

