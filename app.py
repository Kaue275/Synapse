import streamlit as st

with st.container():
    row1 = st.columns(3)

    col1, col2, col3 = row1
   
    with col1:
        options = st.multiselect(
            "Escolha as Métricas",
            ["Resultado", "Cliques", "ROI", "Valor Gasto"],
            ["Resultado", "Valor Gasto"])

    with col2:
        st.write("")

    with col3:
        option = st.selectbox(
            "Selecione a sua franquia",
            ["Franquia Rio Preto", "Franquia Mirassol", "Franquia Bady Bassit"]
        )

st.write("You selected:", options)

st.write("This is outside the container")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Valor das Conversões")
    st.write("R$46,578,23")

with col2:
    st.header("Valor Gasto")
    st.write("R$9,887,27")

with col3:
    st.header("ROI")
    st.write("3.6%")
