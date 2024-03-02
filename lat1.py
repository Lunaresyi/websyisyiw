import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt
#st.write("Syisyi's Interest!")
#df = pd.DataFrame({
#  'No': [1, 2, 3, 4],
#  'Name': ['Rafayel', 'Marius', 'DanHeng', 'Freminet'],
# 'Age': ['24', '21', '27', '20']
#})

#df


def page_1():
  st.title("Page One")
  st.write("This page is for Introduction")
def page_2():
  st.title("Page Two")
  st.write("This page is for Youtbe Video")
def page_3():
  st.title("Page Three")
  st.write("This page is for Math Formula")
  
PAGES = {
  "Page One" : page_1,
  "Page Two" : page_2,
  "Page Three" : page_3
}

st.sidebar.image("htaw.jpg", width=200)
page = st.sidebar.radio("Pages List :", list(PAGES.keys()))
PAGES[page]()