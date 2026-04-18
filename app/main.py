from flask import Flask, render_template, request # Agregamos request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registrar_paciente', methods=['POST'])
def registrar_paciente():
    # Aquí recibimos los datos del formulario (Backend)
    nombre = request.form.get('nombre')
    especie = request.form.get('especie')
    
    # Ejemplo práctico: Por ahora solo confirmamos que llegó
    return f"<h1>Éxito</h1><p>Paciente {nombre} ({especie}) registrado en el sistema.</p><a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)