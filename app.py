import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_plotly_events import plotly_events

st.set_page_config(
    page_title="Help",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/abhiiiman',
        'Report a bug': "https://www.github.com/abhiiiman",
        'About': "## A 'Student Performance and Placement Prediction Tool' by Abhijit Mandal & Divyanshi"
    }
)

# Criando DataFrames para cada cidade
dados_rio_preto = {
    "Métricas": ["Resultado", "Cliques", "ROI", "Valor Gasto"],
    "Valor": ["R$50", "150", "5%", "R$1000"]
}
df_rio_preto = pd.DataFrame(dados_rio_preto)

dados_mirassol = {
    "Métricas": ["Resultado", "Cliques", "ROI", "Valor Gasto"],
    "Valor": ["R$60", "200", "6%", "R$1200"]
}
df_mirassol = pd.DataFrame(dados_mirassol)

dados_bady_bassit = {
    "Métricas": ["Resultado", "Cliques", "ROI", "Valor Gasto"],
    "Valor": ["R$70", "180", "7%", "R$1100"]
}
df_bady_bassit = pd.DataFrame(dados_bady_bassit)

# Dicionário de DataFrames para cada cidade
dfs_cidades = {
    "Franquia Rio Preto": df_rio_preto,
    "Franquia Mirassol": df_mirassol,
    "Franquia Bady Bassit": df_bady_bassit
}

def extrair_metricas(dfs_cidades):
    metricas = {}
    for cidade, df in dfs_cidades.items():
        if 'Resultado' in df["Métricas"].values:
            resultado = df[df["Métricas"] == "Resultado"]["Valor"].values[0]
            metricas[cidade] = resultado
    return metricas

with st.sidebar:
    selected = option_menu(
        menu_title = "Páginas",
        options = ["Menu", "Pesquisar", "Análise de Marketing", "Gestão de Estoque"],
        default_index = 0,
    )

# Inicializando cidade_selecionada e metricas_selecionadas
cidade_selecionada = None
metricas_selecionadas = []

if selected == "Menu":
    # Criando a primeira linha com 2 colunas
    # Criando a primeira linha com 2 colunas
    row1 = st.columns(2)
    with row1[0]:
        metricas = extrair_metricas(dfs_cidades)
        fig, ax = plt.subplots()
        bars = ax.bar(metricas.keys(), metricas.values(), color='skyblue', width=0.7, 
                      edgecolor='grey', linewidth=1.5, capstyle='round')
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                    round(bar.get_height(), 2), ha='center', va='bottom', 
                    color='black', fontsize=10, fontweight='bold')
        ax.set_ylabel('Resultados')
        ax.set_title('Resultados por Cidade')
        plt.xticks(rotation=45)
        st.pyplot(fig)
    with row1[1]:
        st.write('Texto da primeira linha')

    # Criando a segunda linha com 3 colunas
    row2 = st.columns(3)
    with row2[0]:
        st.write('Texto da segunda linha')
    with row2[1]:
        st.write('Texto da segunda linha')
    with row2[2]:
        st.write('Texto da segunda linha')

    # Criando a terceira linha com 3 colunas
    row3 = st.columns(3)
    with row3[0]:
        st.write('Texto da terceira linha')
    with row3[1]:
        st.write('Texto da terceira linha')
    with row3[2]:
        st.write('Texto da terceira linha')

if selected == "Pesquisar":
    col1 = st.columns(1)
    col1[0].title('Pesquisar')
    col1[0].markdown('''
    ####
    Nossa equipe já está trabalhando para que está página comece a rodar o quanto antes!
    ''')

if selected == "Gestão de Estoque":
    col1 = st.columns(1)
    col1[0].title('Gestão de Estoque')
    col1[0].markdown('''
    ####
    Nossa equipe já está trabalhando para que está página comece a rodar o quanto antes!
    ''')

# Informações da métrica selecionada
informacoes_metricas = []

if selected == "Análise de Marketing":
    cidade_selecionada = st.selectbox("Selecione a sua franquia", list(dfs_cidades.keys()))

    metricas_selecionadas = st.multiselect("Escolha as Métricas", dfs_cidades[cidade_selecionada]["Métricas"].tolist(), dfs_cidades[cidade_selecionada]["Métricas"].tolist())

    informacoes_metricas = dfs_cidades[cidade_selecionada].loc[dfs_cidades[cidade_selecionada]["Métricas"].isin(metricas_selecionadas)]

    # Definindo o número máximo de colunas por linha
    max_colunas_por_linha = 3

    # Calculando o número de linhas necessárias
    num_linhas = len(informacoes_metricas) // max_colunas_por_linha
    if len(informacoes_metricas) % max_colunas_por_linha != 0:
        num_linhas += 1

    # Exibindo as informações das métricas selecionadas
    for linha in range(num_linhas):
        # Criando colunas dinâmicas para exibir as métricas
        colunas = st.columns(max_colunas_por_linha)

        # Índice de início das métricas nesta linha
        inicio = linha * max_colunas_por_linha

        # Exibindo as informações das métricas selecionadas na linha atual
        for idx, (_, row) in enumerate(informacoes_metricas.iloc[inicio:inicio + max_colunas_por_linha].iterrows()):
            with colunas[idx]:
                st.header(row["Métricas"])
                st.write(row["Valor"])
