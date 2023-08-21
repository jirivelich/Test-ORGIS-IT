import requests

MEDIAWIKI_API_URL = "https://en.wikipedia.org/w/api.php"

params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': "Python",
        'srlimit': 10
    }

response = requests.get(MEDIAWIKI_API_URL,params=params)

data = response.json()

print(data)