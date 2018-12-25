# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:09:04 2018

@author: laura
"""
#%%
graph={
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
     }

import requests

url = "http://127.0.0.1:5000/{}"

def upload_graph(graph): 
    data=graph
    request=requests.post(url.format("upload_graph"), json=data)
    return request.json()

def degrees_of_separation(origin,destination,graph): 
    data=graph
    request=requests.put("http://127.0.0.1:5000/degrees_of_separation/{}/{}".format(origin,destination), json=data)
    return request.json()

