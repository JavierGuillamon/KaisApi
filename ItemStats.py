# -*- coding: utf-8 -*-
import json

class ItemStats(object):    
    def __init__(self,url):
        
    def create(self,url):    
        with open(url) as json_file:
            stats = json.load(json_file)["data"]["stats"]
    