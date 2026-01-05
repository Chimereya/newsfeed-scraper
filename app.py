from flask import Flask, jsonify
from flasgger import Swagger
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app) # This allows React to talk to Flask


def scrape_hacker_news():
    url = "https://news.ycombinator.com/"
    headers = {'User-Agent': 'Mozilla/5.0'} # Pretend to be a browser
    try:
        response = requests.get(url, headers=headers, timeout=0)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []

        # Select all spans with the titleline class
        links = soup.select('.titleline > a')

        for link in links[:15]: # Getting the top 15 articles
            articles.append({
                "title": link.get_text(),
                "link": link.get('href')
            })
        return articles
        # return [{"title": l.text, "link": l['href']} for l in links[:10]]
    except Exception as e:
        print(f"Scraping error: {e}")
        return []
    

@app.route('/news', methods=['GET'])
def get_news():
    """
    Get the latest Tech News from Hacker News
    ---
    responses:
      200:
        description: A list of news articles
        schema:
          type: array
          items:
            type: object
            properties:
              title:
                type: string
                example: "Show HN: A new web scraper"
              link:
                type: string
                example: "https://news.ycombinator.com/item?id=123"
    """
    data = scrape_hacker_news()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

if __name__== '__main__':
    app.run(debug=True, port=5000)
