from flask import Flask, render_template, jsonify
import pandas as pd

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

@app.route('/historico')
def historico():
    return render_template('historico.html')     # Lê o CSV gerado pelo Python e envia para o template

@app.route('/api/historico')
def api_historico():
    df = pd.read_csv('data/iot_data.csv')
    df = df.tail(100)  # Mostra só as 100 últimas linhas
    return df.to_json(orient='records')

@app.route('/sprints')
def sprints():
    return render_template('sprints.html')


if __name__ == '__main__':
    app.run(debug=True)
