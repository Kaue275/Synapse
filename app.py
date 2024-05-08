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

# Exibindo as informações
st.write("You selected:", metricas_selecionadas)
st.write("This is outside the container")

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
