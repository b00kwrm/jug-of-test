#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import elasticsearch
import json

app = Flask(__name__)
CORS(app)

es = elasticsearch.Elasticsearch(['http://elastic:changeme@elasticsearch:8080'])

@app.route("/", methods=["GET"])
def alldata():
    res = es.search(index="booze", body={"query":{
        "match_all": {}
        }})
    return jsonify(res)

@app.route("/brandsComplete", methods=['GET'])
def brandsComplete():
    """Return unique brand names"""
    res = es.search(index="booze", body={"size": 0,
                                         "aggs": {
                                             "unique_brands": {
                                                 "terms": {
                                                     "field": "brand_name.keyword",
                                                     "size": 100000}}}})

    b = [x['key'] for x in res['aggregations']['unique_brands']['buckets']]
    return jsonify(b)

@app.route("/geoFilter", methods=['POST', 'GET'])
def geoFilter():
    data = request.args.get('q')
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    res = es.search(index="booze", body={"from": 0, "size": 20,
                "query": {
                              "match":{
                                       "brand_name": data }},
                                             "sort": [
                                                 {
                                                     "_geo_distance": {
                                                         "location": {
                                                             "lat": lat,
                                                             "lon": lon
                                                             },
                                                         "order": "asc",
                                                         "unit": "km",
                                                         "distance_type": "plane"
                                                         }}]})
    return jsonify([x['_source'] for x in res['hits']['hits']])

if __name__ == '__main__':
    app.run()

