import random
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data files
nltk.download('punkt')

# Defining the pairs of patterns and responses
patterns_responses = [
    (r'hi|hello|hey|howdy', ['Hello!', 'Hi there!', 'Hey! How can I assist you?']),
    (r'how are you|how are you doing', ['I am just a bot, but I am doing fine!', 'I am doing great! How about you?']),
    (r'what is your name|who are you', ['I am a chatbot.', 'You can call me Bot.', 'I am a friendly chatbot!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!']),
    (r'(.*) your name (.*)', ['My name is ChatBot.', 'I am a chatbot! Nice to meet you!']),
    (r'(.*) help (.*)', ['Sure! How can I assist you today?', 'I am here to help. What do you need assistance with?']),
    (r'(.*) (joke|tell me a joke)(.*)', ['Why don’t skeletons fight each other? They don’t have the guts!', 'Why did the scarecrow win an award? Because he was outstanding in his field!']),
    (r'(.*) (thank you|thanks)(.*)', ['You’re welcome!', 'No problem, happy to help!', 'Anytime!']),
    (r'how old are you', ['I am timeless, I don’t age!', 'I am just a bot, I don’t have an age!']),
    (r'(.*)', ['I didn’t quite understand that.', 'Can you please rephrase that?', 'Sorry, I don’t know how to respond to that.'])
]

# Using NLTK's Chat class to create a chatbot
chatbot = Chat(patterns_responses, reflections)

def start_chat():
    print("ChatBot: Hi! I am a chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        
        # Get a response from the chatbot
        response = chatbot.respond(user_input)
        
        if response:
            print(f"ChatBot: {response}")
        else:
            print("ChatBot: I didn’t understand that. Could you please rephrase?")

if __name__ == "__main__":
    start_chat()
