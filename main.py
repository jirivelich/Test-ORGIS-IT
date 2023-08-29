from flask import Flask, request, jsonify
from src.wikipedia import Wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    return "Wikipedia API" 

@app.route('/search_wikipedia/<lang>/<search>', methods=['GET'])
def search_wikipedia(lang,search):
    
    if not search:
        return jsonify({'error': 'Missing query parameter'}), 400
    
    w = Wikipedia(lang, search)
    
    if w.text() != None and w.is_title():
        return jsonify({"result":f"{(w.text())}"}),200
    
    elif w.text() != None:
        
        return jsonify({'result': None, 'articles': [{'name': f'{w.title()}'}]}),303
    
    else:
        return jsonify({'result': None,}),404


if __name__ == '__main__':
    app.run()