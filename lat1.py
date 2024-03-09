import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4
from page5 import page_5
from page6 import page_6
from img1 import page_7

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
  "Page Three" : page_3,
  "Page Four" : page_4,
  "Page Five" : page_5,
  "Page Six" : page_6,
  "Page Seven" : page_7
  }

st.sidebar.image("fotor-20240303212047.png", width=150)
page = st.sidebar.radio("Pages List :", list(PAGES.keys()))
PAGES[page]()

st.markdown(
  """
      <style>
      [data-testid="stActionButtonIcon"] {
        display: none;
      }
      [data-testid="baseButton-header"] {
        display: none;
      }
        
      </style>
      """,
  unsafe_allow_html=True,)