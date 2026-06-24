print("=== Rule Based AI ChatBot ===")
print("Type 'exit' to quit.\n")

while True:   # loop will run until the user types 'exit'
    user_input = input("You: ") 
    process_string = " ".join(user_input.lower().split()) # Sanitization & making it operable on managing whitespaces and case of character input
    

    
    if process_string == "exit": # Exit condition or loop will terminate here
        print("Bot: Goodbye!")
        break

    
    knowledge_base = { # Knowledge Base
 # Greetings
    "hi": "Hello there!",
    "hii": "Hey!",
    "hiii": "Hey! Nice to see you.",
    "hello": "Hi there!",
    "hey": "Hello!",
    "heyy": "Hey buddy!",
    "yo": "Yo! What's up?",
    "sup": "Not much, what's up with you?",
    "good morning": "Good morning! Hope you have a great day.",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",
    "good night": "Good night! Sweet dreams.",
    "namaste": "Namaste! How can I help you?",

    
    # Asking about bot
    "how are you": "I'm doing great!",
    "how are you doing": "I'm doing well, thanks for asking.",
    "what's up": "Just chatting with you!",
    "who are you": "I'm your Python chatbot.",
    "what is your name": "My name is ChatBot.",
    
    #second loop for Thanks
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "thankyou": "You're welcome!",
    
    # Farewell
    "bye": "Goodbye!",
    "see you": "See you later!",
    "take care": "Take caree!",
    "goodbye": "Bye! Have a nice day.",
    
    
    # Fun
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "are you human": "No, I'm a chatbot.",
    "do you love me": "I like chatting with you!",
    
    # Time
    "what time is it": "Sorry, I cannot check the current time yet.",
    
    # Help
    "help": "You can ask me about greetings, programming, AI, or general questions."
    }

    
    if process_string in knowledge_base: # If-Else Logic for commands & queries
        print("Bot:", knowledge_base[process_string])
    else:
        print("Bot: I don't understand that command.")