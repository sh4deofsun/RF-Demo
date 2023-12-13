import streamlit as st

st.set_page_config(
    page_title="IBTECH QA",
    page_icon='<svg width="48" height="48" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><defs><mask id="ipTCamp0"><g fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4"><path d="M44 35h-4L24 6.5L8 35H4"/><path fill="#555" d="M24 31c-2.761 0-5 3.582-5 8v2h10v-2c0-4.418-2.239-8-5-8Z"/><path d="M4 41h40M15 23s5-4 9-4s9 4 9 4m7-17l-2 3l2 3m0-6l2 3l-2 3M7 17l-1 2l1 2m0-4l1 2l-1 2"/></g></mask></defs><path fill="currentColor" d="M0 0h48v48H0z" mask="url(#ipTCamp0)"/></svg>',
)

if "clicked" not in st.session_state:
    st.session_state.clicked = False


def credential_check(user: str, password: str):
    st.session_state.clicked = (True, )



USER_NAME_INPUT = st.text_input(label="Username",
                                placeholder="USERNAME",
                                key="USERNAME")
USER_PASS_INPUT = st.text_input(label="Password",
                                placeholder="PASSWORD",
                                key="PASSWORD",
                                type="password")
st.button(
    label="Login",
    on_click=credential_check(USER_NAME_INPUT.capitalize(), USER_PASS_INPUT),
)
