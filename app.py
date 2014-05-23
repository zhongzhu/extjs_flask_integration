from flask import Flask, url_for, render_template, jsonify

app = Flask(__name__)

@app.route('/haha', methods=['GET', 'POST'])
def haha():
	list =  [
	{
                        'img': '2004_Porsche_911_Carrera_type_997.jpg',
                        'manufacturer': 'Porsche',
                        'model': '911',
                        'price': 135000,
                        'quality': [
                            {
                                'name': 'overall',
                                'rating': 1
                            },
                            {
                                'name': 'mechanical',
                                'rating': 4
                            },
                            {
                                'name': 'powertrain',
                                'rating': 2
                            },
                            {
                                'name': 'body',
                                'rating': 4
                            },
                            {
                                'name': 'interior',
                                'rating': 3
                            },
                            {
                                'name': 'accessories',
                                'rating': 2
                            }
                        ],
                        'wiki': 'http://en.wikipedia.org/wiki/Porsche_997'
                    }

	]

	return jsonify(data=list)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port=80)