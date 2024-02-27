#general info
COUNTRIES = ['Q30']

#entity info
ENTITY_QUERY_STRING = """
SELECT DISTINCT ?businessLabel ?employees ?profit ?assets ?equity ?markcap

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

	OPTIONAL { ?business wdt:P2295 ?profit. }

	OPTIONAL { ?business wdt:P2403 ?assets. }
	OPTIONAL { ?business wdt:P2137 ?equity. }
	OPTIONAL { ?business wdt:P2226 ?markcap. }

	SERVICE wikibase:label {
		bd:serviceParam wikibase:language "en".
		?business rdfs:label ?businessLabel.
	}
}
GROUP BY ?businessLabel ?employees ?profit ?assets ?equity ?markcap
"""
ENTITY_PATH = 'data/entities_US/{COUNTRY}_3.csv'