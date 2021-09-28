from flask import Flask, render_template, request
from animals import Animals

app = Flask(__name__)
animals = Animals()

@app.route('/')
def index():
    return render_template('index.html', animals=animals)

@app.route('/create', methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form['Name']
        typeId = request.form['TypeId']
        trainerId = request.form['TrainerId']
        level = request.form['Level']
        animals.add_pokemon(name, typeId, trainerId, level)
    return render_template('index.html', animals=animals)

if __name__ == '__main__':
    app.run(debug=True)
