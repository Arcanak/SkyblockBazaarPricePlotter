import json
import requests
import string

all_items_ids = []
for letter in string.ascii_lowercase:
    search = requests.get('https://sky.coflnet.com/api/search/{letter}'.format(letter=letter))
    response = json.dumps(search.json(), indent=4) 
    items = json.loads(response)
    for item in items:
        print(item)
        item_id = item['id']
        all_items_ids.append(item_id)
print("********************************************************************************")
print(all_items_ids)