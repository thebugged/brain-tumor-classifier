
import sqlite3 
import hashlib
import streamlit as st

from PIL import Image 
from multiapp import MultiApp
from apps import alexnet, mobilenet, resnet, xception 

st.set_page_config(
    page_title="Brain Tumour Classifier",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto",
  )


app = MultiApp()

st.title(" Brain Tumour Classifier 🧠")

# app.add_app("AlexNet", alexnet.app)
app.add_app("ResNet152V2", resnet.app)
app.add_app("MobileNetV2", mobilenet.app)
app.add_app("Xception", xception.app)



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
              <style>
			  #MainMenu {visibility: hidden;}
              footer {visibility: hidden;}
              </style>
              """
st.markdown(hide_st_style, unsafe_allow_html=True)



def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False


# DB Management
conn = sqlite3.connect('data.db')
c = conn.cursor()

# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
	


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	
	return data
	


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	conn.commit()
	return data

# Main Function

def main():
	menu = ["Register", "Login"]
	st.sidebar.subheader("Menu Select 🩺")
	choice = st.sidebar.selectbox("",menu)

  


	if choice == "Login":
		st.sidebar.subheader("")
		st.sidebar.subheader("")
		st.sidebar.subheader("")
		
		st.sidebar.subheader("Login")
		st.sidebar.subheader("")

		username = st.sidebar.text_input("Username")
		password = st.sidebar.text_input("Password",type='password')
        
		if st.sidebar.checkbox("Login"):
			create_usertable()
			hashed_pswd = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd))
			conn.commit()

			if result:
				st.sidebar.success("Logged in as {}".format(username))
				conn.commit()

                # The main app
				app.run()

			else:
				st.sidebar.warning("Incorrect Username/Password")
		st.markdown("")
		
	
	

	elif choice == "Register":
		st.markdown('''<h6 style='text-align: left;'>Make Predictions with Convolutional Neural Networks</h6>''', unsafe_allow_html=True)

		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)
		st.markdown('''''', unsafe_allow_html=True)

		st.markdown('''<h5 style='text-align: left;'>Brain Tumour Classifier processes MRI images (PNG,  JPG or JPEG format)</h5>''', unsafe_allow_html=True)
		st.markdown('''<h5 style='text-align: left;'>and determines the type of tumour present (Glioma, Meningioma or Pituary) </h5>''', unsafe_allow_html=True)
		st.markdown('''<h5 style='text-align: left;'>or if there is no tumour present.</h5>''', unsafe_allow_html=True)

		col1, col2, col3 = st.columns(3)
		
		with col1:

			st.markdown('''''', unsafe_allow_html=True)
			
			img = Image.open("brain.jpg")
			st.image(img, width=800)

			st.markdown('')
			st.markdown('')

			

		with col3:
			st.markdown('''<h4 style='text-align: left;'>   Features</h4>''', unsafe_allow_html=True)
			
			st.markdown('''<h6 style='text-align: left;'>   ✔️ Make Predictions</h6>''', unsafe_allow_html=True)
			st.markdown('''<h6 style='text-align: left;'>   ✔️ Record Patient Data</h6>''', unsafe_allow_html=True)
			st.markdown('''<h6 style='text-align: left;'>   ✔️ Save Data in Database</h6>''', unsafe_allow_html=True)
			st.markdown('''<h6 style='text-align: left;'>   ✔️ Login and Registration</h6>''', unsafe_allow_html=True)
		st.sidebar.subheader("")
		st.sidebar.subheader("")
		st.sidebar.subheader("")

		st.sidebar.subheader("Create New Account")
		st.sidebar.subheader("")
		new_user = st.sidebar.text_input("Username")
		new_password = st.sidebar.text_input("Password",type='password')
	
		if st.sidebar.button("Register"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.sidebar.success("You have successfully created a valid Account")
			st.sidebar.info("Select 'Login' in Menu Select")
			conn.commit()

if __name__ == '__main__':
	main()


























  
