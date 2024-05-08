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

import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import plotly.graph_objects as go
import menu
import gestao_estoque
import app as analise_marketing

# Função para criar uma barra lateral com opções
def sidebar_options():
    st.sidebar.title("S.M.A.R.T :rocket:")
    selected = st.sidebar.radio(
        "Menu",
        ["Home", "Upload CSV", "Analysis", "Predictions", "Performance", "Download CSV", "Settings", "Contributors"]
    )
    return selected

def main():
    selected = sidebar_options()

    if selected == "Home":
        st.title('S.M.A.R.T :rocket:')
        st.header("Student Management 🏠 And")
        st.header("Recruitment Tool 🔮")
        st.divider()
        st.header("About :memo:")
        st.markdown('''
        ####
        We are thrilled to introduce you to SMART, your all-in-one solution for student
        management and recruitment needs
        providing a comprehensive platform for tracking academic progress, 
        facilitating career development, and predicting placement opportunities.
        With SMART, educational institutions can efficiently manage student data,
        track their academic performance, and streamline the recruitment process. 
        Meanwhile, students can access personalized career guidance, 
        explore job opportunities, and receive tailored recommendations
        for enhancing their employability. 
        Join us on this exciting journey as we revolutionize
        student management and recruitment with SMART!
        ''')
        
        st.markdown("#### `Get Started Now!`")

    elif selected == "Upload CSV":
        menu.upload_csv()

    elif selected == "Analysis":
        analise_marketing.analysis()

    elif selected == "Predictions":
        menu.predictions()

    elif selected == "Performance":
        menu.performance()

    elif selected == "Download CSV":
        menu.download_csv()

    elif selected == "Settings":
        menu.settings()

    elif selected == "Contributors":
        menu.contributors()

if __name__ == "__main__":
    main()

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