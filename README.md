# AI-CHATBOT-WITH-NLP

COMPANY: CODTECH IT SOLUCTIONS

NAME: SUBHASH K

INTERN ID: CT04DG769

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

As part of my internship at **CodTech IT Solutions Pvt. Ltd.**, I was assigned **Task 3: Build an AI Chatbot using Natural Language Processing (NLP)**. This task involved designing and implementing a basic chatbot capable of interacting with users and responding to their queries using natural language understanding. The goal was to create a simple, text-based assistant that could demonstrate intelligent behavior through keyword-based intent recognition and pattern matching. This task allowed me to apply foundational concepts of **NLP** using Python and popular libraries like **NLTK (Natural Language Toolkit)**, which is a widely-used suite for text processing and language modeling.

To complete the task, I used **Python 3.12.2** and wrote and executed the script using **IDLE Shell**, Python’s default integrated development environment. IDLE is easy to set up and efficient for writing interactive Python programs. The development process began with installing the `nltk` library using the command `pip install nltk`, followed by downloading necessary resources such as the `punkt` tokenizer using `nltk.download('punkt')`, which is essential for breaking text into words or sentences.

The chatbot was built on a simple architecture that included a **knowledge base** of predefined responses and a **set of keyword-intent mappings**. The chatbot identifies the user’s intent by comparing input tokens against a list of common phrases associated with specific categories such as greetings, farewells, requests for help, and identity questions. Based on the matched intent, the chatbot provides an appropriate, randomly selected response from a pool of preset replies. If no match is found, the chatbot falls back on a default reply, ensuring the conversation continues smoothly without breaking.

The core of the chatbot lies in the `match_intent()` function, which tokenizes the user input and compares it with keywords mapped to intents. For example, if a user says, “hi,” the chatbot recognizes the "greeting" intent and responds with “Hey!” or “Hello!” randomly. The chatbot continuously listens for input in a loop until the user types "exit", at which point it gracefully ends the conversation. The `chatbot()` function controls this loop and provides the user interface in the terminal.

From an application perspective, this chatbot serves as a **basic conversational interface**. Though simple, it lays the foundation for more advanced bots that could use **machine learning models** or integrate with larger NLP frameworks like **spaCy**, **Dialogflow**, or **Rasa**. Chatbots similar to this are widely used in **customer support systems**, **FAQ automation**, **educational assistants**, **e-commerce query handling**, and even **personal productivity tools**. When extended further, such bots can also be connected to APIs, databases, or front-end user interfaces (like a web app or mobile app) to create a full-fledged intelligent assistant.

This project not only helped me understand the **basics of natural language processing** but also gave me hands-on experience with **tokenization**, **intent classification**, and **building dialogue systems**. The structure I implemented can be expanded by using more complex matching methods like TF-IDF, cosine similarity, or integrating pre-trained models such as BERT for deep language understanding. Additionally, I learned the value of designing modular, reusable code that can be easily upgraded as the bot's vocabulary or capabilities grow.

In conclusion, **Task 3 helped me strengthen both my programming and NLP skills**. It taught me how natural language data can be interpreted by machines and how a simple chatbot can be made responsive and user-friendly. The task showcased the power of Python in solving real-world problems and gave me valuable insights into how intelligent systems communicate with users in human-like ways.

OUTPUT:

![Image](https://github.com/user-attachments/assets/fba79b5e-980a-4382-905f-13e8a80faa43)
