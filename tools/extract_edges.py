#https://gist.github.com/sirex/b5fdf0228cf03f5b9076b5975c5591a5
from pandas import json_normalize
from SPARQLWrapper import SPARQLWrapper, JSON
from multiprocessing.pool import ThreadPool as Pool
from os import path
from time import sleep
import sys
sys.path.insert(0, '../configs/')
from sparql_config_edges import *

THREAD_COUNT = 5
SLP = .01

def select(query, service='https://query.wikidata.org/sparql'):
		sparql = SPARQLWrapper(service, agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')#saved my ass
		sparql.setQuery(query)
		sparql.setReturnFormat(JSON)
		result = sparql.query().convert()
		return json_normalize(result['results']['bindings'])

def extract_edges(country):
	file_path = EDGE_PATH.format(COUNTRY=country)
	if path.exists(file_path):
		print(country,'edges already exists')
		return
	query = EDGE_QUERY_STRING % country
	print('Querying edges',country)
	data = select(query)
	data.to_csv(file_path)
	print('Saved edges',country)
	sleep(SLP)

#multithreaded extraction
if __name__ == '__main__':
	print('Starting Edge Extraction')
	pool = Pool(THREAD_COUNT)
	pool.map(extract_edges, COUNTRIES)
	pool.close()
	pool.join()
	print('Completed Edge Extraction')
