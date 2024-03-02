import streamlit as st

def page_3():
  st.title("Page Three")
  st.write("This page is for Python Codes from MD(MarkDown) file!!")
  
  with open('hihi.md', 'r') as file:
      isi_teks = file.read()
      st.markdown(isi_teks)