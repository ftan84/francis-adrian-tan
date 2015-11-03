from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def frontpage():
    return render_template('frontpage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
