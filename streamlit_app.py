import streamlit as st
import pandas as pd

st.title("🎈 Davina's new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
color = st.color_picker("Pick A Color", "#F5DFEE")
st.write("The current color is", color)

st.markdown(
    f"""
    <div style="font-family: 'Courier New', Courier, monospace; background-color: #f0f2f6; padding: 15px; border-radius: 5px;">
        <pre>{kode}</pre>
    </div>
    """,
    unsafe_allow_html=True
)
