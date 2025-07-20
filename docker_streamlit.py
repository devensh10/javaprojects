import os 
import streamlit as st
st.title("docker automation tool")
choice=st.sidebar.selectbox("choice",["list container","list images","pull images","run container"])

if choice =="list container":
    if st.button("show container"):
        output=os.popen("docker ps").read()
    
elif choice =="list images":
    if st.button("show images"):
        output=os.popen("docker images").read()
elif choice =="pull images":
    image=st.text_input("enter image name")
    if st.button("pull image"):
        output=os.popen(f"docker pull {image}").read()

elif choice =="run container":
    container=st.text_input("enter container name")
    if st.button("run container"):
        output=os.popen(f"docker run {container}").read()
    

    





 
   