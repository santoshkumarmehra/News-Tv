from django.shortcuts import render
import requests

def index(request):
    access_key = '812880f61ceb6a63dc6dc945c65760d5'
    url = f'http://api.mediastack.com/v1/news?access_key={access_key}&countries=au,us'

    response = requests.get(url)
    news = []

    if response.status_code == 200:
        res = response.json()
        for item in res.get('data', []):
            news.append({
                'title': item.get('title'),
                'description': item.get('description'),
                'image': item.get('image'),
                'url': item.get('url'),
            })

    return render(request, 'newsapp/index.html', {'news': news})
