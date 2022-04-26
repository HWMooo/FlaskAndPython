from flask import Flask, request, jsonify

app = Flask(__name__)

films = [{"name": "Happy Gilmore", "Released":"19/06/1996"}, {"name": "Spiderman: No Way Home", "Released":"20/12/2021"}]

def create(req):
    new_film = req
    films.append(new_film)
    return new_film, 201

@app.route('/')
def welcome():
    return 'Welcome to Flask!!!'

@app.route('/films', methods=['GET', 'POST'])
def films_handler():
    if request.method == 'GET':
        return jsonify(films), 200
    elif request.method == 'POST':
        data = request.json
        statement = create(data)
        return f"you created a film {data['name']}"




if __name__ == '__main__':
    app.run()
