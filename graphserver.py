# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:08:44 2018

@author: laura
"""
#%%
from flask import Flask, jsonify, request
graphserver = Flask("graph server")

@graphserver.route("/upload_graph", methods=["POST"])
def upload_graph():
    body=request.get_json()
    return jsonify(body)
    

@graphserver.route("/degrees_of_separation/<origin>/<destination>", methods=["PUT"])
def degrees_of_separation(origin,destination,graph="",path=[]):
    graph=request.get_json()
    path=path+[origin]
    
    if origin==destination:
        #dofs=degreesofseparation
        dofs=len(path)-int(2)
        if dofs==0:
            return jsonify("These nodes are directly connected")
        else:
            return jsonify(dofs)
    if origin not in graph:
        return jsonify(None)
    for conn in graph[origin]:
        if conn not in path:
            newpath=degrees_of_separation(conn, destination, graph, path)
            if newpath is not None:
                return newpath
    return jsonify(None)

graphserver.run()