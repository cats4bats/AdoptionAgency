from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

class PetForm(FlaskForm):
    """form to handle adding a pet"""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(values=('dog', 'cat', 'porcupine'))])
    photo_url = StringField("Photo Url", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")

class EditPet(FlaskForm):
    """form to handle editing a pet"""


    photo_url = StringField("Photo Url", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")