import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a knowledgeable and motivating gym trainer. You provide personalized workout routines and daily diet plans based on the user's fitness goals, current fitness level, and any dietary restrictions or preferences they have. Always prioritize safety and encourage a healthy lifestyle."),
        ("human", "User Details:\nFitness Goals: {fitness_goals}\nCurrent Fitness Level: {fitness_level}\nDietary Restrictions/Preferences: {dietary_restrictions}\n\nPlease provide a suitable workout routine and daily diet plan.")
    ]
)
with st.sidebar:
    st.write('Virtual Gym Trainer')
    st.image('images.jpg')

st.title('Your Virtual Gym Trainer')
st.balloons()

st.subheader("Let's get started! Please provide some details about yourself:")

fitness_goals = st.text_input("Fitness Goals (e.g., weight loss, muscle gain, improve stamina):")
fitness_level = st.text_input("Current Fitness Level (e.g., beginner, intermediate, advanced):")
dietary_restrictions = st.text_input("Dietary Restrictions/Preferences (e.g., vegetarian, vegan, gluten-free):")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if st.button("Generate Workout and Diet Plan"):
    if fitness_goals and fitness_level:
        response = chain.invoke({
            'fitness_goals': fitness_goals,
            'fitness_level': fitness_level,
            'dietary_restrictions': dietary_restrictions
        })
        st.write(response)
    else:
        st.write("Please fill in all the details to get a personalized plan.")
