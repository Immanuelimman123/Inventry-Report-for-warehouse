from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# -----------------------
# Product Form
# -----------------------
class ProductForm(FlaskForm):
    product_id = StringField('Product ID', validators=[DataRequired()])
    name = StringField('Product Name', validators=[DataRequired()])
    quantity = IntegerField('Product Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit')

# -----------------------
# Location Form
# -----------------------
class LocationForm(FlaskForm):
    location_id = StringField('Location ID', validators=[DataRequired()])
    name = StringField('Location Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# -----------------------
# Product Movement Form
# -----------------------
class ProductMovementForm(FlaskForm):
    movement_id = StringField('Movement ID', validators=[DataRequired()])
    product_id = SelectField('Product', validators=[DataRequired()], coerce=str)
    from_location = SelectField('From Location', coerce=str, choices=[])
    to_location = SelectField('To Location', coerce=str, choices=[])
    qty = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit')
