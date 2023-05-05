from flask import Flask, render_template

app = Flask(__name__)

# Sample data to display on the webpage
data = {
    'name': 'John Doe',
    'age': 30,
    'interests': ['Python', 'Flask', 'Web Development']
}

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='10.0.1.240',debug=True)
