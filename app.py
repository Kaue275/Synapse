import streamlit as st

# FunçãO para seleção das cores, use o color para adicionar a cor 
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

with st.container():
   row1 = st.columns(3)

   col1, col2, col3 = row1
   
   with col1:
    options = st.multiselect(
    "Escolha as Métricas",
    ["Resultado", "Cliques", "ROI", "Valor Gasto"],
    ["Resultado", "Valor Gasto]"])

   with col2:
      st.write("")

   with col3:
       option = st.selectbox(
        "Selecione a sua franquia",
        ("Franquia Rio Preto", "Franquia Mirassol", "Franquia Bady Bassit"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.write("You selected:", options)

st.write("This is outside the container")

col1, col2, col3, = st.columns(3)

with col1:
   st.header("Valor das Conversões")
   st.write("R$46,578,23")

with col2:
   st.header("Valor Gasto")
   st.write("R$9,887,27")

with col3:
   st.header("ROI")
   st.write("3.6%")