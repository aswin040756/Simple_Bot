print("Welcome to this Chatbot!")
C = input("Enter '1' for Simple Bot or '2' for Calculator or '3' for Chatbot or '4' for Average: ")
if C == "1":
    import main
elif C == "2":
    import calc
elif C == "3":
    import Bot
elif C == "4":
    import Avg
else:
    print("Invalid input. Please enter '1', '2', '3', or '4'.")