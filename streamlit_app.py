import streamlit as st
import pandas as pd

# Import Google Font
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.custom-text {
    font-size: 30px;
    color: #232E75;
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


st.title("🎈 Davina's new app")
st.write('<p style="font-size:30px; color:#232E75; font-family:Courier New;">Color Picker</p>',
         unsafe_allow_html=True)
color = st.color_picker("Pick A Color", "#F5DFEE")
st.write("The current color is", color)

