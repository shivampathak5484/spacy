import streamlit as st
import random

import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Predefined responses for chatbot queries
responses = {
    "hello": [
        "Hello! Welcome to the UI/UX Designing Academy chatbot. How can I assist you?",
        "Hi there! How may I help you today?",
        "Greetings! What can I do for you?"
    ],
    "what courses do you offer": [
        "We offer courses like UI Design Fundamentals, Advanced UX Techniques, and Prototyping Tools.",
        "Our courses include UI/UX Design, User Research, and Design Thinking.",
        "We have a variety of courses tailored for aspiring UI/UX designers. Would you like more details?"
    ],
    "how can i enroll": [
        "You can enroll by visiting our website and filling out the application form.",
        "The enrollment process is simple. Contact our admissions team for guidance.",
        "To enroll, check our course schedule online and register for the desired course."
    ],
    "do you offer mentorship programs": [
        "Yes, we provide mentorship programs led by industry experts.",
        "Our mentorship programs are designed to give you hands-on experience with professional guidance.",
        "We offer personalized mentorship to help you succeed in your UI/UX design career."
    ],
    "what are the class schedules": [
        "Our classes are available on weekdays, weekends, and evenings to suit your schedule.",
        "You can choose from flexible class timings. Let me know if you want detailed schedules.",
        "We provide multiple schedules to accommodate working professionals and students."
    ],
    "can you provide course materials": [
        "Yes, all enrolled students receive comprehensive course materials.",
        "We provide access to digital course materials, including templates and case studies.",
        "Course materials are shared through our online portal for easy access."
    ],
    "how can i contact support": [
        "You can contact our support team via email or live chat on our website.",
        "For immediate assistance, call our support helpline.",
        "Reach out to us through the contact form on our website or email us directly."
    ],
    "tell me about feedback": [
        "We value your feedback! Share your thoughts to help us improve our courses.",
        "Feedback is essential to us. After each course, you can submit your suggestions.",
        "You can provide feedback anytime through our feedback portal on the website."
    ],
    "i need help with something complex": [
        "Let me connect you to one of our human representatives for personalized assistance.",
        "For complex queries, I’ll transfer you to a customer support executive.",
        "I’ll notify a human representative to assist you further."
    ],
    "do you operate 24/7": [
        "Yes, our chatbot is available 24/7 to assist you with your queries.",
        "We are here to help you round the clock!",
        "Our chatbot operates continuously, and our support team is available during working hours."
    ]
}

# Function to determine the most similar response
def most_similar_response(user_input):
    user_doc = nlp(user_input)
    max_similarity = -1
    most_similar_response = None

    for query, response in responses.items():
        query_doc = nlp(query)
        similarity = user_doc.similarity(query_doc)

        if similarity > max_similarity:
            most_similar_response = random.choice(response)
            max_similarity = similarity

    similarity_threshold = 0.4
    if max_similarity < similarity_threshold:
        return "I'm sorry, I don't have a response for that."

    return most_similar_response

# Streamlit UI
st.title("UI/UX Designing Academy Chatbot")
st.subheader("Ask me anything about our courses and services!")

# Chat interaction
user_message = st.text_input("Type your message here:")

if user_message:
    response = most_similar_response(user_message)
    st.write("Chatbot:", response)
