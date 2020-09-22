# 프로퍼티는 url, parser, path, api, apikey ==> all str
from dataclasses import dataclass

@dataclass
class Entity:
    
    url : str = ''
    parser : str = ''
    path : str = ''
    api : str = ''
    apikey : str = ''
    