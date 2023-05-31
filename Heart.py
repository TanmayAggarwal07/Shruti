import streamlit as st
import numpy as np
#import matplotlib as plt

def heart_shape():
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    return x, y

x, y = heart_shape()

st.title("I LOVE YOU BBY AND MISS YOU")

fig, ax = plt.subplots()
ax.plot(x, y, color='red')
ax.fill(x, y, color='red')
ax.set_aspect("equal")
ax.axis("off")

st.pyplot(fig)
