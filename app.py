import streamlit as st

with open("mundial2026.html", "r", encoding="utf-8") as f:
    html = f.read()

st.set_page_config(layout="wide", page_title="Mundial 2026")
st.components.v1.html(html, height=900, scrolling=True)
