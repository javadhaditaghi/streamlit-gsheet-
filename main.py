import streamlit as st
from streamlit_gsheets import GSheetsConnection


conn = st.connection("gsheets", type=GSheetsConnection)


data = conn.read(usecols=[0, 1])

st.dataframe(data)
