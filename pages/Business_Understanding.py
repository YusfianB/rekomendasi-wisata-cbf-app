import streamlit as st

st.title("Business Understanding")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Kolom Kiri")
    st.write("Isi kolom pertama")

with col2:
    st.subheader("Kolom Kanan")
    st.write("Isi kolom kedua")