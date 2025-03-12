import streamlit as st
import login
import form

st.set_page_config(page_title = "BWF", 
	page_icon = ":ball:",
	layout="centered",
	initial_sidebar_state= "auto")

pages_dict={"Login":login,
"Application Form":form}

st.sidebar.title("Navigation")
userchoice=st.sidebar.radio("Go to",tuple (pages_dict.keys()))
if userchoice=="Application Form":
	form.app()
else:
	login.app()