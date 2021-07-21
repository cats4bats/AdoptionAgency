from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import PetForm, EditPet

app = Flask(__name__)

app.config['SECRET_KEY'] = '<replace with a secret key>'

toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def show_home_page():
    """displays the home page"""

    pet_list = Pet.query.all()
    return render_template('index.html', pet_list=pet_list)

@app.route('/add', methods=['GET', 'POST'])
def show_add_pet():
    """handling of add pet form"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template('add_pet.html', form=form)

@app.route('/<pet_id>', methods=['GET', 'POST'])
def show_edit_pet(pet_id):
    """handling of edit pet form"""
    pet = Pet.query.get(pet_id)
    form = EditPet(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template('edit_pet.html', form=form, pet=pet)