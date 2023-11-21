from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Ejercicio1', methods=['GET','POST'])
def Ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3

        if asistencia >= 75 and promedio >= 40:
            estado = "ESTUDIANTE APROBADO"
        else:
            estado = "ESTUDIANTE REPROBADO"

        return render_template('Formulario.html', promedio=promedio, estado=estado)
    return render_template('Formulario.html')

@app.route('/Ejercicio2', methods=['GET','POST'])
def Ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        mas_largo = max(nombres, key=len)
        caracteres = len(mas_largo)

        return render_template('Formulario2.html', mas_largo=mas_largo, caracteres=caracteres)

    return render_template('Formulario2.html')

if __name__ == '__main__':
    app.run()
