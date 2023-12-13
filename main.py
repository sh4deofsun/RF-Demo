import streamlit as st

# while(True):
    # st.text(str="Hello")
USER_NAME_INPUT = st.text_input(label="Username", placeholder="USERNAME", key="USERNAME")
USER_PASS_INPUT = st.text_input(label="Password", placeholder="PASSWORD", key="PASSWORD", type='password', )
st.button(label="Login", on_click=print(USER_NAME_INPUT.capitalize()))


# print(USER_NAME_INPUT.capitalize())
