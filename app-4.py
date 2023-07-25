import streamlit as st

st.header('st.multiselect')

options =  st.multiselect(
    'what are your favorite colors?',
    ['red', 'yellow', 'green', 'blue'], 
    ['red', 'yellow'])

st.write('You favorite colors are', options)    