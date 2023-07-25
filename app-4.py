import streamlit as st

st.header('st.multiselect & st.checkbox')

#example 1
st.subheader('st.multiselect')
options =  st.multiselect(
    'what are your favorite colors?',
    ['red', 'yellow', 'green', 'blue'], 
    ['red', 'yellow'])

st.write('You favorite colors are', options)    

#example 2
st.subheader('st.checkbox')

st.write('Pilih makan untuk makan malam !')

nasi_rendang = st.checkbox('Rendang')
nasi_gule = st.checkbox('Gule')
soto_ayam = st.checkbox('Soto Ayam')
ayam_goreng_nashville = st.checkbox('Ayam Goreng Nashville')

if nasi_rendang:
    st.write('You choose Rendang')
if nasi_gule:    
    st.write('You choose Gule')
if soto_ayam:    
    st.write('You choose Soto Ayam')
if ayam_goreng_nashville:
    st.write('You choose Ayam Goreng Nashville')
    
