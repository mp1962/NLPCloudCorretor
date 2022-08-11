import streamlit as st
import gateways

def header():
    st.header('Corrector de estilo')
    st.text('version 0 - Last update 08/08/2022')

def instert_text():
    txt = st.text_area("Escríba aqui")
    colum1, colum2 = st.columns([1,1])
    
    if colum1.button("Corrija y Mejore"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateways.conect_corretor_estilo(txt)
        
            if status == 200:
                st.text_area(label="Texto corregido:", value=new_txt["correction"])
                st.success("¡Corrijido!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpie"):
        st.info("cleaning")

st.sidebar.markdown("# Corretor Estilo ❄️")
header()
instert_text()