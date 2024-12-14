import os
import pandas as pd

# ------------------ Leitura dos arquivos de despesas e receitas ----------------------
# Lê os arquivos de despesas e receitas se existirem no diretório atual
if ('df_despesas.csv' in os.listdir()) and ('df_receitas.csv' in os.listdir()):
    df_despesas = pd.read_csv('df_despesas.csv', index_col=0, parse_dates=True)
    df_receitas = pd.read_csv('df_receitas.csv', index_col=0, parse_dates=True)

# Cria estruturas de dados para receitas e despesas caso os arquivos não existam no diretório atual
else:
    data_structure = {
        'Valor': [],
        'Efetuado':[],
        'Fixo':[],
        'Data':[],
        'Categoria':[],
        'Descrição':[],
    }
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    
    df_receitas.to_csv('df_receitas.csv')
    df_despesas.to_csv('df_despesas.csv')


# ------------------ Leitura dos arquivos de categoria de despesas e receitas ---------------------- 
# Lê os arquivos de categorias de despesas e receitas se existirem no diretório atual e armazena seus valores em listas
if ('df_cat_despesas.csv' in os.listdir())and ('df_cat_receitas.csv' in os.listdir()):
    df_cat_despesas = pd.read_csv('df_cat_despesas.csv', index_col=0)
    df_cat_receitas = pd.read_csv('df_cat_receitas.csv', index_col=0)

    cat_receita = df_cat_receitas.values.tolist()
    cat_despesa = df_cat_despesas.values.tolist()

# Cria estruturas de dados para categorias de receitas e despesas caso os arquivos não existam no diretório atual
else:
    cat_receita = {'Categoria':['Salário', 'Investimentos', 'Comissão']}
    cat_despesa = {'Categoria':['Aluguel', 'Alimentação', 'Lazer', 'Gasolina']}

    df_cat_receita = pd.DataFrame(cat_receita)
    df_cat_despesa = pd.DataFrame(cat_despesa)

    df_cat_receita.to_csv('df_cat_receitas.csv')
    df_cat_despesa.to_csv('df_cat_despesas.csv')
