# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

MEDIAWIKI_API_URL = "https://cs.wikipedia.org/w/api.php"

class Wikipedia:
    
    def __init__(self,search) -> None:
        self.search = search
        self.request = None

    def _request(self, params) -> dict:
        
        if 'action' not in params:
            params['action'] = 'query'
            
        if 'format' not in params:
            params['format'] = 'json'
        
        response = requests.get(MEDIAWIKI_API_URL, params=params)
        json = response.json()
        return json

    def get_page_ID(self) -> tuple|None:
        
        params = {
            'action': 'query',
            'format': 'json',
            'list': 'search',
            'srlimit': 1,
            }
        
        params["srsearch"] = self.search
       
        self.request = self._request(params)
        try:
            page_id = self.request['query']['search'][0]['pageid']
            # print(request)
            return page_id

        except:
            # print(request['query'])
            return None
    
    def _html(self)->str:
        
        if self.get_page_ID != None:
            
            try:
                pageid= self.get_page_ID()
            
                params = {
                    'action': 'query',
                    'format': 'json',
                    'prop': 'revisions',
                    'rvprop': 'content',
                    'rvparse': '',
                    'rvlimit': 1
                    }
                
                params['pageids'] = pageid
                
                request= self._request(params=params)
                html = request['query']['pages'][f'{pageid}']['revisions'][0]['*']
                return html
            
            except:
                return None
        
        return None

    def text(self) -> str:
        
        if self._html() != None:
        
            p= BeautifulSoup(self._html(), 'html.parser').find_all('p')
            html_par = p[0]
            text_ = BeautifulSoup(str(html_par),'html.parser')
            text = text_.get_text(separator= " ",strip = True)
            return text
        
        return None
    
    def is_title(self):
        
        self.get_page_ID()
        
        title = self.request['query']['search'][0]['title']
        print(title)
        
        return self.search.lower() == title.lower()
    
    def title(self):
        try:
            title = self.request['query']['search'][0]['title']
            return title
        except:
            return None
        
    def __str__(self):
        
        if self.text() != None:
            return f'''{self.text()}'''
        
        return "Nebylo nic nalezeno"

if __name__ == "__main__":
    
    pass
  

