from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "clave_secreta_willy"

# Configuración de la Base de Datos
# Esto crea el archivo veterinaria.db dentro de la carpeta 'app'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'veterinaria.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# MODELO DE DATOS (La estructura de tu tabla)
class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(100), nullable=False)
    dueño = db.Column(db.String(100), nullable=False)

# Crear la base de datos automáticamente
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registrar_paciente', methods=['POST'])
def registrar_paciente():
    nombre = request.form.get('nombre')
    especie = request.form.get('especie')
    dueño = request.form.get('dueño')
    
    # GUARDAR EN LA BASE DE DATOS REAL
    nuevo_paciente = Paciente(nombre=nombre, especie=especie, dueño=dueño)
    db.session.add(nuevo_paciente)
    db.session.commit()
    
    flash(f"¡Paciente {nombre} registrado con éxito en la base de datos!")
    return redirect(url_for('registro'))

@app.route('/pacientes')
def listar_pacientes():
    # Consultamos todos los pacientes guardados en la DB
    todos_los_pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes=todos_los_pacientes)

if __name__ == '__main__':
    app.run(debug=True)