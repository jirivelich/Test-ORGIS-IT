from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/search_wikipedia', methods=['GET'])
def search_wikipedia():
    search_query = request.args.get('query')
    if not search_query:
        return jsonify({'error': 'Missing query parameter'}), 400

    wikipedia_api_url = f"https://cs.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={search_query}"
    
    headers = {
        'User-Agent': 'YourAppName/1.0',
        'Accept-Language': 'en-US'  # Změňte na požadovaný jazyk
    }
    
    response = requests.get(wikipedia_api_url, headers=headers)
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run()