import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3

#import pandas as pd
#import matplotlib.pyplot as plt
#st.write("Syisyi's Interest!")
#df = pd.DataFrame({
#  'No': [1, 2, 3, 4],
#  'Name': ['Rafayel', 'Marius', 'DanHeng', 'Freminet'],
# 'Age': ['24', '21', '27', '20']
#})

#df

  
PAGES = {
  "Page One" : page_1,
  "Page Two" : page_2,
  "Page Three" : page_3
}

st.sidebar.image("him.jpg", width=200)
page = st.sidebar.radio("Pages List :", list(PAGES.keys()))
PAGES[page]()