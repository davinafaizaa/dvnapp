import streamlit as st
import pandas as pd

st.title("🎈 Davina's new app")
st.write('<p style="font-size:30px; color:#F5DFEE;">Color Pickert</p>',
unsafe_allow_html=True)
color = st.color_picker("Pick A Color", "#F5DFEE")
st.write("The current color is", color)
