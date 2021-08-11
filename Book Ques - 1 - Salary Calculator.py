B_Salary = float(input("Enter your 'salary' amount : "))
DA = 0.72 * B_Salary
HRA = 0.20 * B_Salary
CCA = 200
Net_Salary = B_Salary + DA + HRA + CCA
PF = 0.08 * B_Salary
Gross_Salary = Net_Salary - PF
print(f'Your gross salary is {Gross_Salary}')
