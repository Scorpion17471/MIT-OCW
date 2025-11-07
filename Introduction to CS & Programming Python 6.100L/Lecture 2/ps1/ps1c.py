## 6.100A PSet 1: Part C
## Name: Ajay Alamuri
## Time Spent: 1 hr
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

down_payment = 800000 * 0.25
max_down, min_down = down_payment + 100, down_payment - 100
r_low, r_high = 0, 1
r = (r_high + r_low) / 2
steps = 1

amount_saved = initial_deposit * ((1 + (r/12))**36)

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

if initial_deposit >= min_down:
    r = 0.0
elif (initial_deposit * (1 + 1/12)**36) < min_down:
    r = None
else:
    while (r_low < r_high):
        if amount_saved < min_down:
            r_low = r
        elif amount_saved > max_down:
            r_high = r
        r = (r_high + r_low) / 2
        steps += 1
        
        amount_saved = initial_deposit * ((1 + (r/12))**36)
        if (amount_saved > min_down and amount_saved < max_down):
            break
        
print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")