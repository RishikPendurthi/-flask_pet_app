from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SECRET_KEY'] = 'secret_key'  # Required for flashing messages
db = SQLAlchemy(app)

# Pet model
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Route to display all pets
@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

# Route to add a pet
@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']

        if not name or not species or not age:
            flash('All fields are required!')
            return redirect(url_for('add_pet'))

        new_pet = Pet(name=name, species=species, age=int(age))
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add_pet.html')

# Route to update a pet
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_pet(id):
    pet = Pet.query.get_or_404(id)

    if request.method == 'POST':
        pet.name = request.form['name']
        pet.species = request.form['species']
        pet.age = request.form['age']

        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_pet.html', pet=pet)

# Route to delete a pet
@app.route('/delete/<int:id>', methods=['POST'])
def delete_pet(id):
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
