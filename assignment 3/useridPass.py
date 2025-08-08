##WAP to check if user has entered correct userid and password.
uid = input("Enter user id:")
password = int(input('Enter password:'))
if uid == "scam" and password == 1234:
    print("Welcome Scammer")
else:
    print("Invalid User ID or Password")
