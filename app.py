import streamlit as st
from faq_data import faq_pairs
from match import get_best_match

st.set_page_config(page_title="FAQ Chatbot", page_icon="💬")
st.title("💬 FAQ Chatbot")
st.write("Ask me anything about our services!")

user_question = st.text_input("Your question:")

if user_question:
    response = get_best_match(user_question, faq_pairs)
    st.markdown(f"**Answer:** {response}")