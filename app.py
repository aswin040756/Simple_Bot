print("Welcome to this Chatbot!")
C = input("Enter '1' for Simple Bot or '2' for Calculator: ")
if C == "1":
    import main
elif C == "2":
    import calc
else:
    print("Invalid input. Please enter '1' or '2'.")
    