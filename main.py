import streamlit as st

st.title("interactive streamlit app")

#taking user input
name = st.text_input("enter your name:")

#displaying a message when a button is clicked
if st.button("submit"):
  st.write(f"hello, {name}! welcome to streamlit.")

