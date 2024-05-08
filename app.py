import streamlit as st
import importlib.util
import pandas as pd

# Função para importar e renderizar a página selecionada
def render_page(page_name):
    module = importlib.import_module(page_name)
    module.render()

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

# Função para renderizar a página de pesquisa
def render_pesquisar():
    st.title("Pesquisar")
    # Adicione aqui o conteúdo da página de pesquisa

# Função para renderizar a página de análise de marketing
def render_analise_marketing():
    st.title("Análise de Marketing")
    st.write("Aqui está a análise de marketing:")
    # Adicione aqui o código que mostra as métricas e outras informações da análise de marketing

# Função para renderizar a página de gestão financeira
def render_gestao_financeira():
    st.title("Gestão Financeira")
    # Adicione aqui o conteúdo da página de gestão financeira

# Definindo um estado para controlar qual página está sendo exibida
state = st.experimental_get_query_params()
page = state.get("page", "menu")

# Criando links para as diferentes páginas
pages = {
    "Menu": "menu",
    "Pesquisar": "pesquisar",
    "Análise de Marketing": "analise_marketing",
    "Gestão de Estoque": "gestao_estoque",
    "Gestão Financeira": "gestao_financeira"
}

selected_page = st.sidebar.radio("Selecione a página:", list(pages.keys()))

# Renderizando a página selecionada
if st.sidebar.button("Reload"):
    st.experimental_set_query_params(page=pages[selected_page])

render_page(pages[selected_page])