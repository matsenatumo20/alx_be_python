user_monthly_income = int(input("Enter your monthly income: "))
user_total_monthly_expenses = int(input("Enter your total monthly expenses: "))
simple_annual_interest_rate = 0.05

monthly_savings = user_monthly_income - user_total_monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * simple_annual_interest_rate)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
