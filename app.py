from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iot')
def iot():
    return render_template('iot.html')

@app.route('/insights')
def insights():
    return render_template('insights.html')

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

if __name__ == '__main__':
    app.run(debug=True)
