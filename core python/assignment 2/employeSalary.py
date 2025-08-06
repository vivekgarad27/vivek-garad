##write a program to calculate totel salary of employee according to da(10%) , ta (12%), hra (15%) of basic salary

basic = int(input("basic salary:"))
da_amt = basic * 0.1
ta_amt = basic * 0.12
hra_amt = basic * 0.15

total_salary = basic + da_amt + ta_amt + hra_amt    

print(f'total salary : {total_salary}')


