import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():

    fact = get_fact()

    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    payload = {"input_text":fact}
    resp = requests.post(url, data=payload, allow_redirects=False)
    heads = resp.headers['location']
    return """<h2>Random sentence:</h2><h4>{}</h4>
              <h2>Pig Latin:</h2>
              <a href={} target="_blank">{}</a>""".format(fact, heads, heads)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

