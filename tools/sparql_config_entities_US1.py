#general info
COUNTRIES = ['Q30']

#entity info
ENTITY_QUERY_STRING = """
SELECT DISTINCT ?business ?businessLabel ?officialname ?origindate


WHERE {
	VALUES ?socialmediatypes {
		wdt:P2013
		wdt:P4264
		wdt:P2002
	}
	?business (wdt:P31/(wdt:P279*)) wd:Q4830453;
		wdt:P17 wd:%s; #rotate this for each country
		?socialmediatypes ?socialmedia;
		wdt:P17 ?country.
	OPTIONAL { ?business wdt:P1128 ?employees. }
	OPTIONAL { ?business wdt:P1448 ?officialname. }
	OPTIONAL { ?business wdt:P571 ?origindate. }

	SERVICE wikibase:label {
		bd:serviceParam wikibase:language "en".
		?business rdfs:label ?businessLabel.
	}
}
GROUP BY ?business ?businessLabel ?officialname ?origindate
"""
ENTITY_PATH = 'data/entities_US/{COUNTRY}_1.csv'