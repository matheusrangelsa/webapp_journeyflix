from flask import Flask, render_template

entrelinhas = Flask(__name__)

@entrelinhas.route('/')
def homepage():
    return render_template("homepage.html")

@entrelinhas.route('/contatos')
def contatos():
    return render_template("contatos.html")

@entrelinhas.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


if __name__ == "__main__":
    entrelinhas.run(debug=True)
