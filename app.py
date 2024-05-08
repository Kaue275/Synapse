import streamlit as st
import pandas as pd

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

# Definindo um estado para controlar qual página está sendo exibida
import streamlit as st
import pandas as pd

# Função para renderizar a página de menu
def render_menu():
    st.title("Menu")
    # Adicione aqui o conteúdo da página de menu

# Função para renderizar a página de pesquisa
def render_pesquisar():
    st.title("Pesquisar")
    # Adicione aqui o conteúdo da página de pesquisa

# Função para renderizar a página de análise de marketing
def render_analise_marketing():
    st.title("Análise de Marketing")
    st.write("Aqui está a análise de marketing:")
    # Adicione aqui o código que mostra as métricas e outras informações da análise de marketing

# Função para renderizar a página de gestão de estoque
def render_gestao_estoque():
    st.title("Gestão de Estoque")
    # Adicione aqui o conteúdo da página de gestão de estoque

# Função para renderizar a página de gestão financeira
def render_gestao_financeira():
    st.title("Gestão Financeira")
    # Adicione aqui o conteúdo da página de gestão financeira

# Definindo um estado para controlar qual página está sendo exibida
state = st.experimental_get_query_params()
page = state.get("page", "menu")

# Criando links para as diferentes páginas
menu_link = st.sidebar.button("Menu")
pesquisar_link = st.sidebar.button("Pesquisar")
analise_marketing_link = st.sidebar.button("Análise de Marketing")
gestao_estoque_link = st.sidebar.button("Gestão de Estoque")
gestao_financeira_link = st.sidebar.button("Gestão Financeira")

# Renderizando a página apropriada com base no link clicado
if menu_link:
    page = "menu"
elif pesquisar_link:
    page = "pesquisar"
elif analise_marketing_link:
    page = "analise_marketing"
elif gestao_estoque_link:
    page = "gestao_estoque"
elif gestao_financeira_link:
    page = "gestao_financeira"

# Atualizando a URL para refletir a página atual
if st.button("Reload"):
    st.experimental_set_query_params(page=page)

# Renderizando a página selecionada
if page == "menu":
    render_menu()
elif page == "pesquisar":
    render_pesquisar()
elif page == "analise_marketing":
    render_analise_marketing()
elif page == "gestao_estoque":
    render_gestao_estoque()
elif page == "gestao_financeira":
    render_gestao_financeira()
