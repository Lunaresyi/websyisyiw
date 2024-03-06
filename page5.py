import streamlit as st

def page_5():
    st.title(": ̗̀➛Aplikasi Menghitung Persegi Panjang༊*·˚")
    
    panjang = st.number_input ("Input Panjangღ", 0)
    lebar = st.number_input ("Input Lebarღ", 0)
    hasil = st.button ("Hitung!ღ")
    if hasil :
        luas = panjang * lebar
        st.write ("Your Result˚₊· ͟͟͞͞➳❥ : ", luas)