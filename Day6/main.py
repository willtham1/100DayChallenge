print("LOGIN FORM")
print("Please enter your credentials to login")
username = input("Username: ")
password = input("Password: ")

if username == "will" and password == "1234":
    print("Welcome Will!")
elif username == "carmen" and password == "4321":
    print("Welcome Carmen!")
elif username == "admin" and password == "admin":
    print("Welcome Admin!")
else:
    print("Invalid credentials. Go away!")


## Day7 was all about elif statements and how to use them more in depth.