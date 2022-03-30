from flask import Flask, render_template, request, redirect, url_for
import requests
from urllib.parse import urlencode

app = Flask(__name__)

host = "https://qiita.com"
path = "/api/v2/items"


app = Flask(__name__)
@app.route('/')
def index():
    query = request.args.get("query")

    #全記事を入れるリストを作成
    articlelist = []

    parameters = {
        'per_page': 20,
        'query': query
    }

    r = requests.get(host + path + "?" + urlencode(parameters))
    r.raise_for_status()
    items = r.json()

    hoge = "検索結果: " + (query if query else "")

    return render_template('index.html',articlelist=items,hoge=hoge)

if __name__ == "__main__":
    app.run(debug=True)