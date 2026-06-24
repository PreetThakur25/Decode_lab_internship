
raw_input=input('you: ')




while True:
    user_input=raw_input 
    if user_input == 'exit':
        break
    process_string=raw_input.lower().strip()  ###sanatization of raw data provided by the user

    



    response= {'hello': 'Hi there!',
    'how are you?' : 'I am fine, thank you!',
    'what is your name?' : 'My name is ChatBot',
    'bye' : 'Goodbye!',
    'thank you' : 'You are welcome!'
} 
if process_string in response:
    print('bot', response[process_string])
else:
    print('bot', 'I don\'t understand!')