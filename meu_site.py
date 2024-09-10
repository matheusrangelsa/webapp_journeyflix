from flask import Flask, render_template, request
import csv
from filtragem_colaborativa import pre_lista_filmes, recomendacao

app = Flask(__name__)
# route -> nomedosite.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
@app.route("/journeyflix")
def journeyflix():
    return render_template('journeyflix.html')

# Função para ler o arquivo CSV
def read_csv(file_name):
    with open(file_name, encoding='utf-8') as file:
        return list(csv.DictReader(file))

@app.route('/resultado', methods=['POST'])
def resultado():
    trajeto = float(request.form['trajeto'])
    categorias_preferidas = request.form.getlist('Categorias')
    print(categorias_preferidas)
    data_set = read_csv('base_de_dados_conteudos.csv')
    filtro = pre_lista_filmes(data_set, categorias_preferidas, trajeto)
    pre_lista = [filtro]
    resultado = recomendacao(pre_lista, trajeto)

    print(resultado)

    # Aqui você pode inserir seu código de filtro para gerar a lista de resultados
    return render_template('resultado.html', resultados=resultado)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

