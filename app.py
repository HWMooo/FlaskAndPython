from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Flask!!!'

@app.route('/films', methods=['GET', 'POST'])
def films_handler():
    if request.method == 'GET':
        return jsonify([{"name": "Happy Gilmore", "Realeased":"19/06/1996"}, {"name": "Spiderman: No Way Home", "Realeased":"20/12/2021"}]), 200
    elif request.method == 'POST':
        data = request.json
        return data.name




if __name__ == '__main__':
    app.run()
