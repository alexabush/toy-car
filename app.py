from flask import Flask, render_template, url_for, redirect, request
from flask_modus import Modus
from car import Car

cars = [Car('Toyota', 'Corolla', 2005), Car('Toyota', 'Corolla S', 2005),
 Car('Toyota', 'Corolla', 2012)]

app = Flask(__name__)
modus = Modus(app)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/cars/new')
def new():
    return render_template('new.html')

@app.route('/cars', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        make = request.form.get('make')
        model = request.form.get('model')
        year = request.form.get('year')
        cars.append(Car(make, model, year))
        return redirect(url_for('index'))
    else:
        return render_template('index.html', cars=cars)

@app.route('/cars/<int:id>' , methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    for car in cars:
        if car.id == id:
            target_car = car
    if request.method == 'GET':
        return render_template('show.html', car=target_car)
    elif request.method == b'PATCH':
        target_car.make = request.form['make']
        target_car.model = request.form['model']
        target_car.year = request.form['year']
        return redirect(url_for('index'))
    elif request.method == b'DELETE':
        cars.remove(target_car)
        return redirect(url_for('index'))

@app.route('/cars/<int:id>/edit')
def edit(id):
    for car in cars:
            if car.id == id:
                target_car = car
    return render_template('edit.html', car=target_car)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
