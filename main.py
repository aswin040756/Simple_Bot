print("simple bot created ...." )
print("Bot is running ....")
while True:
    a = input("YOU: ")
    if a == "Thanks" or a == "thanks" or a == "Thank you" or a == "thank you":
        print("Bot is shutting down ....")
        break
    elif a == "Hello" or a == "hello" or a == "Hi" or a == "hi":
        print("Bot: Hello, How can I help you?")
    elif a == "How are you?" or a == "how are you?":
        print("Bot: I am fine, Thank you for asking.")
    elif a == "What is your name?" or a == "what is your name?":
        print("Bot: My name is Bot.")
    elif a == "What can you do?" or a == "what can you do?":
        print("Bot: I can answer your questions and have a conversation with you.")
    elif a == "What is the time?" or a == "what is the time?":
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Bot: The current time is", current_time)
    else:
        print("Bot: I am sorry, I don't understand that.")
