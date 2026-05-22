import streamlit as st
import pandas as pd

st.title("🎈 Davina's new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
color = st.color_picker("Pick A Color", "#000000")
st.write("The current color is", color)

from numpy.random import default_rng as rng

df = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": rng(0).standard_normal(20),
        "col3": rng(1).standard_normal(20),
    }
)

st.bar_chart(
    df,
    x="col1",
    y=["col2", "col3"],
    color=["#EFDFF5", "#0000FF"],)

from vega_datasets import data

source = data.barley()

st.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)
