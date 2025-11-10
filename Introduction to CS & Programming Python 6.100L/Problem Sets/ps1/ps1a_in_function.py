def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	return months