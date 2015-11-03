from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def frontpage():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
