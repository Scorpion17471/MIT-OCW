## 6.100A PSet 1: Part A
## Name: Ajay Alamuri
## Time Spent: 10 min
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

# Annual
yearly_salary = float(input("Enter your yearly salary: "))
# Static
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# Static
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

# Static
portion_down_payment = 0.25
# Monthly
amount_saved = 0
# Annual
r = 0.05

down_payment = portion_down_payment * cost_of_dream_home

monthly_salary_saved = (yearly_salary / 12) * portion_saved

# Output
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved < down_payment:
    monthly_return = monthly_salary_saved + (amount_saved * (r / 12))
    amount_saved += monthly_return
    months += 1

print(f"Number of months: {months}")