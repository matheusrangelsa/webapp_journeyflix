from time import sleep
from tqdm import tqdm # usar para barra de progresso
import pandas as pd
import random # para usar a função "random.shuffle" do módulo 
import csv
import os

# seleção de categorias
def genero():
    # Imprime as opções de gênero
    print('\n ---------- SELECAO DE GENEROS ------------\n')

    options = {
        'Genero': 'Acao,Comedia,Drama,Ficcao Cientifica,Romance,Suspense,Terror'.split(','),
        'Codigo': [int(i) for i in range(1, 8)] 
    }

    genero = pd.DataFrame(data = options)
    # formatando a saída para escolha dos generos
    print(genero.to_string(index = False)) 
    # Lê a seleção de gêneros feita pelo usuário
    selecione = input('\nEscolha os gêneros abaixo digitando os número correspondentes separados por vírgula: ').replace(' ', '').split(",") # tratando a entrada do usuario
    opcao_selecionada = []

    # Verifica se a seleção do usuário é válida e adiciona à lista de gêneros escolhidos
    for s in selecione:
      if int(s) in list(genero.Codigo):
        g = genero[genero.Codigo == int(s)].Genero.unique()[0]
        opcao_selecionada.append(g)

    # Imprime a lista de gêneros escolhidos ou uma mensagem de erro caso não haja seleções válidas
    if opcao_selecionada:
        genero_selecionado = genero.loc[genero.Genero.isin(opcao_selecionada)]
        print("\n --------- Categorias favoritas ----------- \n")

        print(genero_selecionado.to_string(index = False))
        print("\n ----------------------------------------- \n")
        sleep(0.5)
    else:
        print("Nenhuma opção válida selecionada.")
    
    return opcao_selecionada

def pre_lista_filmes(data_set, categorias_preferidas, tempo_trajeto):
    # Cria uma lista vazia para armazenar os resultados
    filtro_inicial = [movie for movie in data_set if movie['Categoria'] in categorias_preferidas and int(movie['Duracao']) <= tempo_trajeto]
    # Uso da função "random.shuffle" do módulo "random" para embaralhar a ordem da lista antes de retorná-la
    random.shuffle(filtro_inicial)
    return filtro_inicial

# Segundo filtro que retorna apenas os filmes que se somados preenchem o tempo de trajeto
def lista_filmes(pre_lista, tempo_trajeto):
    resultado = []
    for filme in pre_lista[0]:
        duracao = int(filme['Duracao'])
        if duracao <= tempo_trajeto:
            resultado.append(filme)
            tempo_trajeto -= duracao
        if tempo_trajeto == 0:
            break
    return resultado


  

  