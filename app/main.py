from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_vcvets' # Esto es vital para los mensajes flash

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
    flash(f'¡Paciente {nombre} ({especie}) registrado con éxito!')
    return redirect(url_for('registro'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)