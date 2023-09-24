import streamlit as st
import os
import random
from googletrans import Translator
import chatbotCore  # Import the modified chatbotCore module

page_bg_img = """
<style>

    [data-testid="stAppViewContainer"]{
    
    font-family: 'Share Tech', sans-serif;
    font-size: 35px;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
    width: 100vw;
    height: 100vh;
    text-shadow: 8px 8px 10px #0000008c;
    background-color: #343a40;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='49' viewBox='0 0 28 49'%3E%3Cg fill-rule='evenodd'%3E%3Cg id='hexagons' fill='%239C92AC' fill-opacity='0.25' fill-rule='nonzero'%3E%3Cpath d='M13.99 9.25l13 7.5v15l-13 7.5L1 31.75v-15l12.99-7.5zM3 17.9v12.7l10.99 6.34 11-6.35V17.9l-11-6.34L3 17.9zM0 15l12.98-7.5V0h-2v6.35L0 12.69v2.3zm0 18.5L12.98 41v8h-2v-6.85L0 35.81v-2.3zM15 0v7.5L27.99 15H28v-2.31h-.01L17 6.35V0h-2zm0 49v-8l12.99-7.5H28v2.31h-.01L17 42.15V49h-2z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"), linear-gradient(to right top, #343a40, #2b2c31, #211f22, #151314, #000000);

}
 
   
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
#st.set_page_config(page_title="Multi-Page Landing", layout="wide")

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
