import streamlit as st

def page_4():
  st.markdown("<h1 style='text-align: center; color: Black;'>₊˚ପ⊹Page Four˚୨୧⋆</h1>", unsafe_allow_html=True)
  st.markdown('*<div style="text-align: center; color: gray; ">Vibing with some music༉‧₊˚.*', unsafe_allow_html=True)
  st.audio("sys.mp3.mp3")
  st.markdown('*<div style="text-align: center; color: gray; ">Want some more?*ੈ✩‧₊˚', unsafe_allow_html=True)
  with st.container():
   st.image("Untitled68 (1).png", width=520)
  left_co, cent_co,last_co = st.columns(3)
  with cent_co:
    st.link_button("₊˚ପ⊹Click Here˚୨୧ ⋆", "https://open.spotify.com/playlist/3Qd6vi4FqNmxwTtxntTpha?si=EYVzRGqFTuC9lDyxpREkdg&pi=a-xtl5Yl6WTpyjlit.io/gallery")
