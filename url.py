import requests
import urllib.parse

API_KEY = "AIzaSyBJhXjJX0VoxE-PutAD8JGPG5fk7QYismg"
CX = "823e4e07ae9ee47bc"   

def get_urls(query, max_results=10):
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={encoded_query}"

    response = requests.get(url)

    urls = []
    if response.status_code == 200:
        data = response.json()
        cnt = 0
        for item in data.get("items", []):
            if cnt >= max_results:
                break
            urls.append(item["link"])
            cnt += 1
    else:
        print("Error:", response.status_code, response.text)

    return urls
