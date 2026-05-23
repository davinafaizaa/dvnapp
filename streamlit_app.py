import streamlit as st
import pandas as pd

st.title("🎈 Davina's new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
color = st.color_picker("Pick A Color", "#F5DFEE")
st.write("The current color is", color)
st.background_color ("F5DFEE")

