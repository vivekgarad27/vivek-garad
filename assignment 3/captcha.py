##WAP to check whether the captcha is correct or not
import random

uid = input("Enter your User ID:")
pwd = int(input("Enter your Password:"))


if uid == "admin" and pwd == 1234:
    print("User id and password is correct")
    
    captcha = random.randint(1111, 9999)
    print(f"Captcha: {captcha}")
    
    user_captcha = int(input("Enter your Captcha: "))
    
    if user_captcha == captcha:
        print("Login Successful")
    else:
        print("Invalid Captcha! Login Failed")
else:
    print("Invalid User ID or Password! Login Failed")
