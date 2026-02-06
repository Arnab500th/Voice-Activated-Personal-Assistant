import requests
from config import NEWS_API_KEY as key
base_url ="https://newsapi.org/v2/everything?q=india&language=en&sortBy=publishedAt&apiKey="


def get_news():
    url=base_url+key
    responce = requests.get(url)
    if responce.status_code ==200:
        data = responce.json()
        articles = data.get("articles",[])

        if not articles:
            return []
        
        headlines = []
        for i in range(min(5,len(articles))):
            headlines.append(articles[i]["title"])
        return headlines

    else:
        return None


