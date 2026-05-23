import streamlit as st
import pandas as pd

# CSS untuk background
st.markdown("""
<style>
.stApp {
    background-color: #F5DFEE;
}
</style>
""", unsafe_allow_html=True)

st.title("🎈 Davina's new app")
st.write('<p style="font-size:30px; color:#232E75; font-family:Serif;">Color Picker</p>',
         unsafe_allow_html=True)
color = st.color_picker('<p style="font-size:25px">Pick A Color, "#F5DFEE"</p>)
st.write("The current color is", color)

