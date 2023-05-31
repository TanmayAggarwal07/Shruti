import streamlit as st
import numpy as np

def heart_shape():
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    return x, y

x, y = heart_shape()

st.title("I LOVE YOU BBY AND MISS YOU")

st.plotly_chart({
    "data": [
        {"x": x, "y": y, "type": "scatter", "fill": "toself", "fillcolor": "red"}
    ],
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "showlegend": False,
        "width": 500,
        "height": 500,
        "plot_bgcolor": "white"
    }
})
