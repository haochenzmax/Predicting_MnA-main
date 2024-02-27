#general info
COUNTRIES = ['Q30']

#entity info
ENTITY_QUERY_STRING = """
SELECT DISTINCT ?businessLabel ?country
(GROUP_CONCAT(DISTINCT ?industry; SEPARATOR = ", ") AS ?industries)
(GROUP_CONCAT(DISTINCT ?ceo; SEPARATOR = ", ") AS ?ceos)
(GROUP_CONCAT(DISTINCT ?chair; SEPARATOR = ", ") AS ?chairs)
(GROUP_CONCAT(DISTINCT ?hq; SEPARATOR = ", ") AS ?hqs)
(GROUP_CONCAT(DISTINCT ?group; SEPARATOR = ", ") AS ?groups)
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

	OPTIONAL { ?business wdt:P452 ?industry. }

	OPTIONAL { ?business wdt:P159 ?hq. }
	OPTIONAL { ?business (p:P169/ps:P169) ?ceo. }
	OPTIONAL { ?business wdt:P488 ?chair. }
	OPTIONAL { ?business wdt:P361 ?group. }
	SERVICE wikibase:label {
		bd:serviceParam wikibase:language "en".
		?business rdfs:label ?businessLabel.
	}
}
GROUP BY ?businessLabel ?country
"""
ENTITY_PATH = 'data/entities_US/{COUNTRY}_2.csv'