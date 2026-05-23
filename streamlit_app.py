import streamlit as st
import pandas as pd

st.title("🎈 Davina's new app")
st.write('<p style="font-size:30px; color:#232E75; font:Serif">Color Picker</p>',
unsafe_allow_html=True)
color = st.color_picker("Pick A Color", "#F5DFEE")
st.write("The current color is", color)

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap'); 

html, body, [class*="css"] {
    font-family: 'Roboto', sans-serif; 
    font-size: 18px;
    font-weight: 500;
    color: #091747;
