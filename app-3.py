import streamlit as st

st.header('st.selectbox')

# Example 1
option1 = st.selectbox(
    "what is your favorite color?",
    ('red', 'yellow', 'green', 'blue', 'indigo', 'violet'))
st.write('You favorite color is', option1)

# Example 2

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    
col1,col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option2 = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
st.write('you like to be contacted by', option2)