import requests
import json
from bs4 import BeautifulSoup

headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }
url = "https://www.instagram.com/p/CSJghW0AnPV/"
main_url = f"{url}?__a=1"
response = requests.get(main_url, headers=headers)
print(response.status_code)
if response.ok:
    r = response.json()
    pic_url = r['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
    name = r['graphql']['shortcode_media']['owner']['username']
    lst = []
    # for i in name:
    #     name2 = i['node']['edges']
    #     lst.append(name2)
    print(name)
