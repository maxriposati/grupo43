from wtforms import Form, StringField, SubmitField, validators

class Formulario_Producto(Form):
    id = StringField('Id', [validators.DataRequired()])
    nombre = StringField('Nombre', [validators.DataRequired()])
    precio = StringField('Precio', [validators.DataRequired()])
    existencia = StringField('Existencia', [validators.DataRequired()])
    enviar = SubmitField('Agregar producto')