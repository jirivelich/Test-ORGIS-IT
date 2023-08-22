from flask import Flask, request, jsonify, abort
import src.julits as ulits
import requests



app = Flask(__name__)

@app.route('/search_wikipedia/<lang>/', methods=['GET'])
def search_wikipedia(lang):
    search_query = request.args.get('query')
  
    if not search_query:
        return jsonify({'error': 'Missing query parameter'}), 400
    
    wikipedia_api_url = f"https://{lang}.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={search_query}"
    # wikipedia_api_url = f"https://{lang}.wikipedia.org/w/rest.php/v1/page/{search_query}"
    
    response = requests.get(wikipedia_api_url)
    
    data = response.json()
    
    # text = ulits.stdout_encode(data["source"])
    
    print(len(data["query"]['search']))
    print(response.text)
    print(response.url)
    
    return data,response.status_code


if __name__ == '__main__':
    app.run()