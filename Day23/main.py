def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "admin" and password == "1234":
            print("Login successful!")
            break
        else:
            print("Invalid credentials, please try again.")
            continue

print("Relit Login")
login()

#Day 23 we learned about definition essentially a function just like javascript.