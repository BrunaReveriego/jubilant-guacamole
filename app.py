from flask import Flask, render_template

app = Flask('teste')

LISTA = [
    'Item 1',
    'Item 2',
    'Item 3'
]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ola')
def ola():
    resposta = '<h1>Ola Mundo no Flask</h1>'
    resposta += '<ul>'

    for item in LISTA:
        resposta += '<li>' + item + '</li>'
    resposta += '</ul>'
    return resposta

app.run(debug=True)