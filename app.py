from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)

Bootstrap(app)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/anotherpage')
def another_page():
    return render_template('another_page.html')


if __name__ == '__main__':
    app.run(debug=True)