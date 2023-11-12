from flask import Flask, render_template, request
from Controllers import cadastroController

app = Flask(__name__)
@app.route('/')
def cadastro():
    return render_template("cadastroUsuario.html")

@app.route('/cadastroUsuario', methods = ["POST"])
def cadastroPost():
    nome = request.form['nome']
    dataNascimento = request.form['dataNascimento']
    parentesco = request.form['parentesco']
    #fotoPerfil = request.form['fotoPerfil'] #fotoPerfil
    familia = cadastroController.cadastrarUsuario(nome, dataNascimento, parentesco)
    return render_template('cadastroIntegrante.html'), familia

@app.route('/cadastroFamilia', methods = ["POST"])
def cadastroFamilia():
    nomeintegrante = request.form['nomeintegrante']
    dataNascimentoIntegrante = request.form['dataNascimentoIntegrante']
    parentescoIntegrante = request.form['parentescoIntegrante']
    #fotoPerfilIntegrante = request.form['fotoPerfilIntegrante'] #fotoPerfilIntegrante
    cadastroController.cadastrarIntegrante(nomeintegrante,dataNascimentoIntegrante,
                                           parentescoIntegrante)
    return render_template('cadastroIntegrante.html')

@app.route('/dashboard', methods = ['GET'])
def dashboard():
    cadastroController.mostrarDashboard()
    return render_template('Dashboard.html')

app.run()