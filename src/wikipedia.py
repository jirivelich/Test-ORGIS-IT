# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup



class Wikipedia:
    
    def __init__(self,lang,search) -> None:
        self.search = search
        self.request = None
        self.lang = lang

    def _request(self, params) -> dict:
        
        if 'action' not in params:
            params['action'] = 'query'
            
        if 'format' not in params:
            params['format'] = 'json'
        
        response = requests.get(f"https://{self.lang}.wikipedia.org/w/api.php", params=params)
        # print(response.text)
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
            print(page_id)
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
                # print(html)
                return html
            
            except:
                return None
        
        return None
    
    

    def text(self) -> str|None:
        html_par = None
        
        if self._html() != None:
        
            p= BeautifulSoup(self._html(), 'html.parser').find_all('p')
            
            for index in range(len(p)):
                html_par = p[index]
                if "<b>" in str(html_par):
                    break
                else:
                    html_par = p[0]
                    print("V odstavci se nenachazí tučné písmo")
                
            text_ = BeautifulSoup(str(html_par),'html.parser')
            text = text_.get_text(separator= " ",strip = True)
            print("text:", text)
            return text
        
        return None
    
    def is_title(self) ->bool:
        
        self.get_page_ID()
        try:
        
            title = self.request['query']['search'][0]['title']
            return self.search.lower() == title.lower()
        
        except:
            return False
    
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
  

