import streamlit as st
def app():
	st.title("Email Login")
	email=["guna2323@gmail.com","sruthi09@gmail.com","killbil@gmail.com","gsr155@gmail.com"]
	password=["gffgh","fdfP_f","DHsDsih","finsta"]
	user_pass=dict(zip(email,password))
	Email=st.text_input("Gmail")
	Password=st.text_input("Password")
	if st.button("Login"):
		if (Email==""):
			st.warning("Email feild is empty")
		else:
			if(Password==""):
				st.warning("Password feild is empty")
			else:
				if Email in email:
	#in keyword checks the input of user and matches the emails in the list
					if Password==user_pass[Email]:
					#email is key and the we r accessing values using [] method
						st.success("Login successful")
					else:
						st.warning("Password is inccorect")
				else:
					st.warning("Email is not in the data base")