import streamlit as st
from datetime import datetime, time

st.header('st.slider')

st.subheader('Slider')
# Example 1    
age=st.slider('How old are you?', 0, 130, 25) # min: 0, max: 130, default: 25
st.write("I'm ", age, ' years old') # print the value of age

#Example 2
st.subheader('Range slider')

values = st.slider(
    'select a range of values',
    0.0, 100.0, (25.0, 75.0))  # min: 0.0, max: 100.0, default: (25.0, 75.0)
st.write('values : ', values)
    
#Example 3
st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45))) # min: 0h, max: 23h, default: 17h
st.write("You're scheduled for:", appointment) # print the value of appointment

#Example 4
st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value=(datetime(2023, 7, 25, 11, 30)),
    format="MM/DD/YY - hh:mm") #show date time in this format
st.write("Start time:", start_time) # print the value of start_time

#Example 5
import streamlit as st

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))

st.write('You selected wavelengths between', start_color, 'and', end_color)