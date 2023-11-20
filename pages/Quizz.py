import streamlit as st

st.title("Welcome to my quizz, let's do it !")

st.subheader("Question 1 : ")
with st.form("question1"):
    reponse1 = st.text_input("What is the colour of the white horse of Napoléon ?")
    button = st.form_submit_button("Confirm")
if button:
    if reponse1.lower() == "white":
        st.write("Yep yep")
    else:
        st.write("Hell nah")

st.subheader("Question 2 : ")
with st.form("question2"):
    reponse2 = st.text_input("How many hair does Thanos have ?")
    button = st.form_submit_button("Confirm")
if button:
    if reponse2.lower() == "0":
        st.write("Yep yep")
    else:
        st.write("Hell nah")

st.subheader("Question 3 : ")
with st.form("question3"):
    reponse3 = st.text_input("We are going to die before Luffy becomes the Pirates' King : yes (y) or no (n) ?")
    button = st.form_submit_button("Confirm")
if button:
    if reponse3.lower() == "y":
        st.write("Yep yep")
    else:
        st.write("Hell nah")