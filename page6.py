import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

def page_6():
    st.markdown("<h1 style='text-align: center; color: Black;'>₊˚ପ⊹Page Six˚୨୧⋆</h1>", unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; color: gray; ">₊˚ପ⊹My top 5 in thingsੈ✩‧₊˚', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; color: gray; ">₊˚ପ⊹In here I will put some of things I like and rate them by sections! I will pt my top 5 only!✩‧₊˚', unsafe_allow_html=True)
    st.write(" ")
    st.markdown('<div style="text-align: center; color: gray; ">₊˚ପ⊹My top 5 Booksੈ✩‧₊˚', unsafe_allow_html=True)
    st.write(" ")
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        df = pd.DataFrame({
        'No': [1, 2, 3, 4, 5],
        'Title': ['The Adventure of Sherlock Holmes ', 'The Body in Library', 'The World According to Anna', 'Bumi Series', 'Kisah 1001 Malam'],
        'Rating': ['★★★★★', '★★★★★', '★★★★☆', ' ★★★★☆', '★★★☆']
        })
        st.dataframe(df)
        
    st.write(" ")
    st.markdown('<div style="text-align: center; color: gray; ">₊˚ପ⊹My top 5 Movieੈ✩‧₊˚', unsafe_allow_html=True)
    left_co, cent_co,last_co = st.columns(3)
    st.write(" ")
    with cent_co:
        df = pd.DataFrame({
        'No': [1, 2, 3, 4, 5],
        'Title': ['Sherlock Holmes BBC Version', 'Aquaman and The Lost Kingdom (2023)', 'Harry Potter and The Wizarding World (Series)', 'Wanted (2008)', 'The Hunger Games (Series)'],
        'Rating': ['★★★★★', '★★★★★', '★★★★☆', '  ★★★★', '★★★★']
        })
        st.dataframe(df)