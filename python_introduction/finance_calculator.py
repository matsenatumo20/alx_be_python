monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
simple_annual_interest_rate = 0.05

monthly_savings = int(monthly_income) - int(monthly_expenses)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * simple_annual_interest_rate)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
