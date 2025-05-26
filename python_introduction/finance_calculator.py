# Prompt the user for monthly income
monthly_income_str = input("Enter your monthly income: ")
monthly_income = float(monthly_income_str) # Convert to float to handle decimal incomes

# Prompt the user for total monthly expenses
monthly_expenses_str = input("Enter your total monthly expenses: ")
monthly_expenses = float(monthly_expenses_str) # Convert to float

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Assume a simple annual interest rate
annual_interest_rate = 0.05 # 5% as a decimal

# Calculate Projected Annual Savings
# Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Output Results
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f for 2 decimal places
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
