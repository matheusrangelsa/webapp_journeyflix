from flask import Flask, render_template, request
import csv
from filtro_filmes import pre_lista_filmes, lista_filmes

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
@app.route("/entrelinhas")
def entrelinhas():
    return render_template('entrelinhas.html')

# Sem importar desse jeito, não funciona e também desisti por enquanto de entender o porque
def read_csv(file_name):
    with open(file_name, encoding='utf-8') as file:
        return list(csv.DictReader(file))

@app.route('/resultado', methods=['POST'])
def resultado():
    trajeto = int(request.form['trajeto'])
    categorias_preferidas = request.form.getlist('Categorias')
    print(categorias_preferidas)
    data_set = read_csv('filmes_projeto - filmes_projeto.csv')
    filtro = pre_lista_filmes(data_set, categorias_preferidas, trajeto)
    pre_lista = [filtro]
    resultado = lista_filmes(pre_lista, trajeto)
    print(resultado)

    # Aqui você pode inserir seu código de filtro para gerar a lista de resultados
    return render_template('resultado.html', resultados=resultado)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

