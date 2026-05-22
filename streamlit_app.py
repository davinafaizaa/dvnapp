import streamlit as st
import pandas as pd

st.title("🎈 Davina's new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
color = st.color_picker("Pick A Color", "#000000")
st.write("The current color is", color)

from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.bar_chart(df)
