from flask import Flask, render_template

app = Flask(__name__)


@app.route('/componente1')
def data():
    dictionary = {
        'gold': 'Todo Incluido Be Gold',
        'title': 'Puente Real',
        'subtitle': 'Lovers Club',
        'icons': 'class:"icons"'
    }

    datos = []

    for valor in dictionary.values():

        datos.append(valor)


    return render_template(
        'index.html', datos=datos)


if __name__ == '__main__':
    app.run(debug=True)
