from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Make API request
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()

    # Render template with API data
    return render_template('index-api.html', posts=data)

if __name__ == '__main__':
    app.run(host='10.0.1.240',debug=True)
