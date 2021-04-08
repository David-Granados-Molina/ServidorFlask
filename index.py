from flask import Flask, render_template

app = Flask(__name__)


@app.route('/componente1')
def data():
    dictionary = {'gold': 'Todo Incluido Be Gold', 'title': 'Puente Real', 'subtitle': 'Lovers Club',
                  'icons': 'class:"icons"'}

    return render_template(
        'index.html',
        gold=dictionary['gold'],
        title=dictionary['title'],
        subtitle=dictionary['subtitle'],
        icons=dictionary['icons']
    )


if __name__ == '__main__':
    app.run(debug=True)
