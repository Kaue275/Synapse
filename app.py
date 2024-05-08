import streamlit as st

# FunçãO para seleção das cores, use o color para adicionar a cor 
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.write("Valor das Conversões")

with col2:
   st.header("A dog")
   st.write("Valor das Conversões")

with col3:
   st.header("An owl")
   st.write("Valor das Conversões")