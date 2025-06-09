import nltk
from nltk.tokenize import word_tokenize
import random
nltk.download('punkt_tab')

responses = {
    'greeting': ['Hello!', 'Hi there!', 'Hey!', 'Greetings!'],
    'name': ['I am CodTechBot.', 'You can call me CodTechBot.', 'CodTechBot at your service.'],
    'help': ['I can answer simple questions. Ask me anything!', 'What do you want to know?'],
    'goodbye': ['Goodbye!', 'See you later!', 'Have a great day!'],
    'default': ["Sorry, I didn't understand that. Can you ask something else?"]
}

keywords = {
    'greeting': ['hello', 'hi', 'hey', 'greetings'],
    'name': ['your name', 'who are you', 'what is your name'],
    'help': ['help', 'can you help', 'what can you do'],
    'goodbye': ['bye', 'goodbye', 'see you'],
}

def match_intent(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    for intent, keys in keywords.items():
        for key in keys:
            if all(word in user_input for word in key.split()):
                return intent
    return 'default'

def chatbot():
    print("CodTechBot: Hi! I'm your assistant. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("CodTechBot: Goodbye! Have a nice day.")
            break

        intent = match_intent(user_input)
        reply = random.choice(responses[intent])
        print(f"CodTechBot: {reply}")

if __name__ == "__main__":
    chatbot()
