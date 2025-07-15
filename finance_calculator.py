# Prompt user for financial inputs
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest
annual_savings = monthly_savings * 12
interest_rate = 0.05
projected_savings = annual_savings + (annual_savings * interest_rate)

# Output results
print(f"\nYour monthly savings are: ${monthly_savings:.2f}")
print(f"Projected savings after one year (with 5% interest): ${projected_savings:.2f}")