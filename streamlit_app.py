import streamlit as st
import pandas as pd

def set_custom_font(font_url, font_name):
    custom_css = f"""
    <style>
    @font-face {{
        font-family: '{font_name}';
        src: url('{font_url}');
    }}
    html, body, [class*="st-"] {{
        font-family: '{font_name}', sans-serif;
    }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Contoh memuat font dari URL eksternal
set_custom_font("https://fonts.google.com/", "Playwrite México Guides")


st.title("🎈 Davina's new app")
st.write('<p style="font-size:30px; color:#232E75;">Color Picker</p>',
         unsafe_allow_html=True)
color = st.color_picker("Pick A Color", "#F5DFEE")
st.write("The current color is", color)

