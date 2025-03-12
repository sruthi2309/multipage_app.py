import streamlit as st
def app():
	st.title("Badminton Application Form")
	Name=st.text_input("Student Name: ")
	Gender= st.selectbox("Gender:",("Select","Male","Female"))
	#creats a input box 
	Parents=st.text_input("Parents Name: ")
	st.write("Date of birth: ")
	beta_col1, beta_col2, beta_col3 = st.beta_columns(3)
	with beta_col1:
		Date=st.selectbox("Date: ", (range(0,32)))
	with beta_col2:
		Month=st.selectbox("Month:", (range(0,12)))
	with beta_col3:
		Year=st.text_input("Year:")

	st.slider("Height in cm", 60,180)
	Address=st.text_input("Address:")
	number=st.text_input("Contact number:")
	st.multiselect("Skills",("Left handed","Right handed","Good grip","Excellent grip","Good footwork","Excellent footwork"))
	#select will only allowe u to select 1 item while mulit select will allowe u to to chooese more than one thing
	if st.button("Submit"):
		if (Name=="" | Gender=="Select" | Parents=="" | Date==0 | Month==0 | Year=="" | Address=="" | number==""):
			st.warning("Some fields are empty")
		else:
			st.success("Your form has been submitted")
			st.write("We shall contact You soon for further information")