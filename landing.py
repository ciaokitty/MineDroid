import streamlit as st
import os
import random
from googletrans import Translator
import chatbotCore  # Import the modified chatbotCore module

st.set_page_config(page_title="Multi-Page Landing", layout="wide")

menu = st.sidebar.selectbox("Navigation", ["Home", "ChatBot", "PDF_Reader", "Contact"])

facts = ["The average modern electronic device has more than 35 minerals in it.","The first metals to be unearthed were gold and copper.","The oldest known mine is believed to be the Lion Cave in Swaziland","In the future, mining could extend beyond Earth like the possibility of mining asteroids","India has a long history of mining, with evidence of mining activities dating back to the Indus Valley Civilization around 3000 BCE.","Rare earth elements, essential for electronics and renewable energy technologies, are actually not rare, but they are challenging to mine and extract.","Silicon, the most well-known mineral used in electronics, is used for manufacturing semiconductors and microchips, which are the brains behind electronic devices.","Miners once used canaries to detect dangerous gases in coal mines. If the canary stopped singing or died, it was a sign of unsafe conditions.","Miners have a rich tradition of creating songs to pass the time and communicate underground. These songs are known as pit music or miners hymns.","Coal has been used for heating for centuries, and it played a significant role in keeping homes warm during the Industrial Revolution.","Pink diamonds are among the rarest and most valuable gemstones in the world."]

def home_page():
    st.title("🤖 MineDroid")
    st.header("Welcome to the Home Page!")
    st.write("### Select your Option from the Sidebar selectbox! 😃")
    st.write("#### We have 3 features available!")
    st.write("#### 1) Chat Bot")
    st.write("#### 2) PDF Reader")
    st.write("#### 3) You can use the application on the Mobile Remote device")
    
def chatbot_page():
    st.title("🤖 ChatBot Page")
    st.write("This is the Chat_Bot Page. Here, you can ask your queries in any language.")
    
    # Create a text input field for user queries
    user_input = st.text_input("Enter your query:")
    
    if st.button("Ask"):
        if user_input:
            st.write("#### Fun fact while the bot's thinking! \n " + facts[random.randint(0,len(facts)-1)])
            response = chatbotCore.run_chatbot(user_input)  # Call the chatbot function
            st.write("## Bot's Response:")
            st.write("#### " + response)
        else:
            st.warning("Please enter a query before clicking 'Ask'.")

def pdf_reader():
    st.title("📖 PDF Reader!")
    st.write("This is the PDF reader!")
    st.write("Here, you can upload any PDF of yours and ask questions regarding it!")

def contact_page():
    st.title("Contact Page")
    st.write("Contact us at contact@example.com")

if menu == "Home":
    home_page()
elif menu == "ChatBot":
    chatbot_page()
elif menu == "PDF_Reader":
    pdf_reader()
elif menu == "Contact":
    contact_page()
