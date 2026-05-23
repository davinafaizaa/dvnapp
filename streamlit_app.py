import streamlit as st
import pandas as pd

st.title("🎈 Davina's new app")
st.write('<p style="font-size:30px; color:#232E75; style="font:Serif;">Color Picker</p>',
unsafe_allow_html=True)
color = st.color_picker("Pick A Color", "#F5DFEE")
st.write("The current color is", color)



