from flask import Flask, render_template

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/globoplay/entrelinhas")
def entrelinhas():
    return render_template('entrelinhas.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    trajeto = int(request.form['trajeto'])
    # Aqui você pode inserir seu código de filtro para gerar a lista de resultados
    resultados = ['Resultado 1', 'Resultado 2', 'Resultado 3']
    return render_template('resultado.html', resultados=resultados)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

