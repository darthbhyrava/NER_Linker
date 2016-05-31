# -*- coding: utf-8 -*-
from SPARQLWrapper import SPARQLWrapper, JSON

import urllib2

'''
proxy = urllib2.ProxyHandler({'http': 'proxy.iiit.ac.in'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

#if the arg is empty in ProxyHandler, urllib will find itself your proxy config.
proxy_support = urllib.request.ProxyHandler({'http': 'proxy.iiit.ac.in'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
'''



sparql = SPARQLWrapper("http://dbpedia.org/sparql")
#sparql = SPARQLWrapper("http://10.3.1.91:8890/sparql")

sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/India> dbp:leaderName ?label }
""")
print '\n\n*** JSON Example'
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print result["label"]["value"]
