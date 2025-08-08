##WAP to accept age of five people and also per person ticket amount . Then find the total ticket amount for all five people.
##children below 12 = 30% discount
##sinior citizen above 59 = 50% discount
##others need to pay full ticket amount
age1 = int(input("Enter age of person 1:"))
age2 = int(input("Enter age of person 2:"))
age3 = int(input("Enter age of person 3:"))
age4 = int(input("Enter age of person 4:"))
age5 = int(input("Enter age of person 5:"))
ticket_amt = int(input("Enter ticket amount :"))

total_amount = 0
#For person 1
if(age1 < 12):
    dis_amt = ticket_amt * 0.3
    total_amt = ticket_amt - dis_amt
elif(age1 >59):
    dis_amt = ticket_amt * 0.5
    total_amt = ticket_amt - dis_amt
else:
    total_amt = ticket_amt

person1 = total_amt
#For person 2
if(age2 < 12):
    dis_amt = ticket_amt * 0.3
    total_amt = ticket_amt - dis_amt
elif(age2 >59):
    dis_amt = ticket_amt * 0.5
    total_amt = ticket_amt - dis_amt
else:
    total_amt = ticket_amt

person2 = total_amt

#for person 3
if(age3 < 12):
    dis_amt = ticket_amt * 0.3
    total_amt = ticket_amt - dis_amt
elif(age3 >59):
    dis_amt = ticket_amt * 0.5
    total_amt = ticket_amt - dis_amt
else:
    total_amt = ticket_amt

person3 = total_amt

#For person 4
if(age4 < 12):
    dis_amt = ticket_amt * 0.3
    total_amt = ticket_amt - dis_amt
elif(age4 >59):
    dis_amt = ticket_amt * 0.5
    total_amt = ticket_amt - dis_amt
else:
    total_amt = ticket_amt

person4 = total_amt

#For person 5
if(age5 < 12):
    dis_amt = ticket_amt * 0.3
    total_amt = ticket_amt - dis_amt
elif(age5 >59):
    dis_amt = ticket_amt * 0.5
    total_amt = ticket_amt - dis_amt
else:
    total_amt = ticket_amt

person5 = total_amt

print(person1 + person2 + person3 + person4 + person5)
