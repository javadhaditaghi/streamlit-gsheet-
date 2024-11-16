
import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

title = st.text_input("Section", "Name of the section")
st.write("This section has been added: ", title)

fullName = st.text_input("Full Name", "Full name of the collaborator")
st.write("This collaborator has been added: ", fullName)


if st.button("Add to Spreadsheet"):
    if title and fullName:
        data = conn.read()


        new_row = [title, fullName]
        updated_data = data.append(new_row)


        conn.write(updated_data)
        st.success("New row added to the spreadsheet!")
    else:
        st.error("Please fill out both fields before submitting.")

data = conn.read()
st.write("Current Data in Spreadsheet:")
st.dataframe(data)