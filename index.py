from flask import Flask, render_template

app = Flask(__name__)


@app.route('/componente1')
def data():
    dictionary = {
        'gold': 'Todo Incluido Be Gold',
        'title': 'Puente Real',
        'subtitle': 'Lovers Club',
        'icons': 'class:"icons"',
        'pictures': [
            {
                'image': '../static/img/img1.svg',
                'name': 'img1'
            },
            {
                'image': '../static/img/img2.svg',
                'name': 'img2'
            },
            {
                'image': '../static/img/img3.svg',
                'name': 'img3'
            },
            {
                'image': '../static/img/img4.svg',
                'name': 'img4'
            }
        ]
    }

    return render_template('index.html', **dictionary)


if __name__ == '__main__':
    app.run(debug=True)
