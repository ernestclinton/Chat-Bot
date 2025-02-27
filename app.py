import streamlit as st

# Title for the chatbot
st.title("Simple FAQ Chatbot")

# Define chatbot responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "product": ["We offer various services including AI solutions, consulting, and software development."],
    "pricing": ["Our services start at $99/month. Contact us for a customized quote."],
    "hi": ["Hello! How can I assist you today? Do you have any questions or need help with something specific?"]
}

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return responses["hello"]
    elif "product" in user_input or "service" in user_input:
        return responses["product"]
    elif "price" in user_input or "cost" in user_input:
        return responses["pricing"]
    elif "hi" in user_input or "contact" in user_input:
        return responses["hi"]
    else:
        return ["I'm sorry, I don't understand that. Can you please rephrase?"]

# User input
user_input = st.text_input("Ask me a question:")

if st.button("Submit"):
    if user_input:
        bot_response = get_response(user_input)
        for response in bot_response:
            st.write(response)