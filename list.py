import requests

url = "https://imdb8.p.rapidapi.com/v2/search"

querystring = {"searchTerm":"game","type":"NAME","first":"5"}

headers = {
	"x-rapidapi-key": "9da9b05cb6msh36b46c773430828p12266ajsn89915f9bdc25",
	"x-rapidapi-host": "imdb8.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
# print(data.mainSearch.edges)
results = []
main_search_edges = data.get('mainSearch', {}).get('edges', [])
for edge in main_search_edges:
        node = edge.get('node', {})
        entity = node.get('entity', {})
        name_text = entity.get('nameText', {}).get('text', '')
        primary_image = entity.get('primaryImage', {}).get('url', '')
        
        known_for_edges = entity.get('knownFor', {}).get('edges', [])
        known_for_titles = []
        for kf_edge in known_for_edges:
            kf_node = kf_edge.get('node', {})
            title_text = kf_node.get('title', {}).get('titleText', {}).get('text', '')
            known_for_titles.append(title_text)
        
        results.append({
            'name': name_text,
            'image': primary_image,
            'known_for': known_for_titles
        })
# print(results)

for result in results:
    print(result.name,'+++++++++++++++++++++++++++++++++++++')
# for title in result.known_for:
#      print(title,'========') 
# image_url = data.get('results', [])