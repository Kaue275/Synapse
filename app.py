import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

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

# Dropdown para selecionar a cidade
cidade_selecionada = st.selectbox("Selecione a sua franquia", list(dfs_cidades.keys()))

# Multiselect para selecionar as métricas
metricas_selecionadas = st.multiselect("Escolha as Métricas", dfs_cidades[cidade_selecionada]["Métricas"].tolist(), dfs_cidades[cidade_selecionada]["Métricas"].tolist())

# Informações da métrica selecionada
informacoes_metricas = dfs_cidades[cidade_selecionada].loc[dfs_cidades[cidade_selecionada]["Métricas"].isin(metricas_selecionadas)]



with st.sidebar:
    selected = option_menu(
        menu_title = "Páginas",
        options = ["Menu", "Pesquisar", "Análise de Marketing", "Gestão de Estoque"],
        default_index = 0,
    )

if selected == "Menu":
    col1 = st.columns(1)
    col1[0].title('Menu')
    col1[0].markdown('''
    ####
    Nossa equipe já está trabalhando para que está página comece a rodar o quanto antes!
    ''')

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
if selected == "Análise de Marketing":

    # Layout de 2 linhas com 3 colunas
    row1 = st.columns(3)
    row2 = st.columns(3)

    # Exibindo as informações das métricas selecionadas em 2 linhas
    for index, row in informacoes_metricas.iterrows():
        if index < 3:
            with row1[index]:
                st.header(row["Métricas"])
                st.write(row["Valor"])
        else:
            with row2[index-3]:
                st.header(row["Métricas"])
                st.write(row["Valor"])