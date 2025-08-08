s1 = int(input("Enetr first subject marks:"))
s2 = int(input("Enetr second subject marks:"))
s3 = int(input("Enetr third subject marks:"))
s4 = int(input("Enetr fourth subject marks:"))
s5 = int(input("Enetr ffifth subject marks:"))

total_marks = s1 + s2 + s3 + s4 + s5

percentage = (total_marks / 500) * 100
print("Percentage is: ", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
elif percentage >= 50:
    print("Grade : E")
elif percentage >= 40:
    print("Grade: F")
else:
    print("your are fail.\nyou are looser \ttry again next time.")    
