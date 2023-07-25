import streamlit as st
import random

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

# Define the checkboxes
nasi_rendang = st.checkbox('Rendang')
nasi_gule = st.checkbox('Gule')
soto_ayam = st.checkbox('Soto Ayam')
ayam_goreng_nashville = st.checkbox('Ayam Goreng Nashville')

# Create a list of selected options
selected_options = []
if nasi_rendang:
    selected_options.append('Rendang')
if nasi_gule:    
    selected_options.append('Gule')
if soto_ayam:    
    selected_options.append('Soto Ayam')
if ayam_goreng_nashville:
    selected_options.append('Ayam Goreng Nashville')

# Display the "Randomize" button
if st.button('Randomize'):
    # Randomly choose one option from the selected ones
    if selected_options:
        random_choice = random.choice(selected_options)
        st.write(f'Anda memilih makan malam: {random_choice}')
    else:
        st.write('Silakan pilih makanan untuk makan malam!')
