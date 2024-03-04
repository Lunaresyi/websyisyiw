import streamlit as st

def page_3():
  st.markdown("<h1 style='text-align: center; color: Black;'>₊˚ପ⊹Page Three˚୨୧⋆</h1>", unsafe_allow_html=True)
  st.markdown('*<div style="text-align: center; color: gray; ">ˏˋ°•*⁀➷This page is for Python Codes from MD(MarkDown) file!!⍣ ೋ',  unsafe_allow_html=True)

  with open('hihi.md', 'r') as file:
      isi_teks = file.read()
      st.markdown(isi_teks)