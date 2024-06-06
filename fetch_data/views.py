from django.shortcuts import render

# Create your views here.
import requests

from movies.models import Movies

def fetch_data(req):
    url = "https://imdb8.p.rapidapi.com/v2/search"
    querystring = {"searchTerm": "game", "type": "NAME", "first": "10"}

    headers = {
        "x-rapidapi-key": "9da9b05cb6msh36b46c773430828p12266ajsn89915f9bdc25",
        "x-rapidapi-host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json().get('data', {}).get('mainSearch', {}).get('edges', [])
    
    results = []
    for edge in data:
        node = edge.get('node', {}).get('entity', {})
        name_text = node.get('nameText', {}).get('text', '')

        known_for = node.get('knownFor', {}).get('edges', [])
        for kf_edge in known_for:
            kf_node = kf_edge.get('node', {})
            title_text = kf_node.get('title', {}).get('titleText', {}).get('text', '')
            # id = kf_node.get('title', {}).get('title', {}).get('id', '')
            release_year = kf_node.get('title', {}).get('releaseYear', {}).get('year', '')
            # release_date = kf_node.get('title', {}).get('releaseDate', {}).get('day', '')
            # release_month = kf_node.get('title', {}).get('releaseDate', {}).get('month', '')
            rating = kf_node.get('title', {}).get('ratingsSummary', {}).get('aggregateRating', '')
            title_image_url = kf_node.get('title', {}).get('primaryImage', {}).get('url', '')
            # print(rating,'------------------------->>>')
            item, created = Movies.objects.update_or_create(
                genre=name_text,
                title=title_text,
                defaults={
                    
                    'release_year': release_year,
                    'rating': rating,
                    'title_image_url': title_image_url,
                }
            )