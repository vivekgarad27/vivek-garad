p  = int(input("Enter princpal:"))
t  = int(input("Enter time:"))
r  = int(input("Enter rate:"))

ci = p*( (1+r/100)**t)-p

print(f'compound interest : {ci}.')