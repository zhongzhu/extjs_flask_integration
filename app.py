import os
from flask import Flask, url_for, render_template, jsonify

app = Flask(__name__)

@app.route('/haha', methods=['GET', 'POST'])
def haha():
    list =  [
    {
                        'img': '2004_Porsche_911_Carrera_type_997.jpg',
                        'manufacturer': 'Porsche',
                        'model': 911,
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
                    },
                    {
                        'img': '250px-Nissan_GT-R.jpg',
                        'manufacturer': 'Nissan',
                        'model': 'GT-R',
                        'price': 80000,
                        'quality': [
                            {
                                'name': 'overall',
                                'rating': 2
                            },
                            {
                                'name': 'mechanical',
                                'rating': 3
                            },
                            {
                                'name': 'powertrain',
                                'rating': 5
                            },
                            {
                                'name': 'body',
                                'rating': 4
                            },
                            {
                                'name': 'interior',
                                'rating': 2
                            },
                            {
                                'name': 'accessories',
                                'rating': 2
                            }
                        ],
                        'wiki': 'http://en.wikipedia.org/wiki/Nissan_Gt-r'
                    },
                    {
                        'img': '250px-BMW_M3_E92.jpg',
                        'manufacturer': 'BMW',
                        'model': 'M3',
                        'price': 60500,
                        'quality': [
                            {
                                'name': 'overall',
                                'rating': 3
                            },
                            {
                                'name': 'mechanical',
                                'rating': 5
                            },
                            {
                                'name': 'powertrain',
                                'rating': 3
                            },
                            {
                                'name': 'body',
                                'rating': 4
                            },
                            {
                                'name': 'interior',
                                'rating': 5
                            },
                            {
                                'name': 'accessories',
                                'rating': 3
                            }
                        ],
                        'wiki': 'http://en.wikipedia.org/wiki/Bmw_m3'
                    },
                    {
                        'img': '250px-Audi_S5.jpg',
                        'manufacturer': 'Audi',
                        'model': 'S5',
                        'price': 53000,
                        'quality': [
                            {
                                'name': 'overall',
                                'rating': 4
                            },
                            {
                                'name': 'mechanical',
                                'rating': 1
                            },
                            {
                                'name': 'powertrain',
                                'rating': 1
                            },
                            {
                                'name': 'body',
                                'rating': 4
                            },
                            {
                                'name': 'interior',
                                'rating': 1
                            },
                            {
                                'name': 'accessories',
                                'rating': 5
                            }
                        ],
                        'wiki': 'http://en.wikipedia.org/wiki/Audi_S5#Audi_S5'
                    },
                    {
                        'img': '250px-2007_Audi_TT_Coupe.jpg',
                        'manufacturer': 'Audi',
                        'model': 'TT',
                        'price': 40000,
                        'quality': [
                            {
                                'name': 'overall',
                                'rating': 5
                            },
                            {
                                'name': 'mechanical',
                                'rating': 2
                            },
                            {
                                'name': 'powertrain',
                                'rating': 2
                            },
                            {
                                'name': 'body',
                                'rating': 3
                            },
                            {
                                'name': 'interior',
                                'rating': 4
                            },
                            {
                                'name': 'accessories',
                                'rating': 1
                            }
                        ],
                        'wiki': 'http://en.wikipedia.org/wiki/Audi_TT'
                    }                    

    ]

    return jsonify(data=list)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@app.route('/data/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('CarListings/data', path))    

if __name__ == '__main__':
    app.debug = True
    app.run(port=80)