#New file push, 
#new files
#git add DreamChartiot.py
#git commit -m "Initial commit of Macro-Jamborie.py"
#git push origin main

#update file
# save file
# git add Macro-Jamborie.py 
# git commit -m "Updated logic in Macro-Jamborie.py"
# git push origin main

# Define companies 'Vitals' 
# Tech Start up called Macro-Jamborie

# Financial Vitals
# Financial Vitals
total_assets = 500000  # Cash, equipment, etc.
total_liabilities = 200000  # Loans, bills to pay
annual_cash_flow = 75000  # Money left over at the end of the year
shares_outstanding = 10000  # Total number of stock "slices"

# equity value (Book value)
equity_value = total_assets - total_liabilities

# to get market value, we often use a multiple of cash flow, say 10x for a tech startup (industry based)
# earnings based value = annual_cash_flow * 10
# total coompany value = equity value + earnings based value
total_company_value = equity_value + (annual_cash_flow * 10)
#print(f"Total Company Value: ${total_company_value}")

# whole pizzq, now we want to find what slice is worth 
# divide total value by shares outstanding
total_sharesoutstanding = 10000
value_per_share = total_company_value / total_sharesoutstanding
#print(f"Value Per Share: ${value_per_share}")

# risk (margin of safety)
risk_margin = 0.2  # 20% margin of safety
adjusted_value_per_share = value_per_share * (1 - risk_margin)
#print(f"Adjusted Value Per Share (with margin of safety): ${adjusted_value_per_share}")

# "what if" machine - sensitivity analysis
# if cash flow multiple changes from 10x to 5x 
def calculate_intrinstic_value(cash_flow, assets, liabilities, shares, multiple=10, margin=0.2):
    # Calculate Equity (Book Value)
    equity_value = assets - liabilities
    # Calculate Total Value (Equity + Multiplier effect)
    total_company_value = equity_value + (cash_flow * multiple)
    # Calculate Per Share
    price_per_share = total_company_value / shares
    # Apply Margin of Safety
    safe_price = price_per_share * (1 - margin)
    return safe_price

intrinsic_value = calculate_intrinstic_value(annual_cash_flow, total_assets, total_liabilities, shares_outstanding, multiple=5, margin=0.4)
print(f"Intrinsic Value Per Share with 5x multiple and 40% margin of safety: ${intrinsic_value}")

#compare to real stock price
market_price = 50 
if intrinsic_value > market_price:
    print("The stock is undervalued. Consider buying.")
else:
    print("The stock is overvalued. Consider waiting or selling.")

#calculate a 10% buffer
upper_bound = intrinsic_value * 1.1
lower_bound = intrinsic_value * 0.9

if market_price < lower_bound:
    print("🟢 The stock is significantly undervalued. Strong buy signal.")
elif lower_bound <= market_price <= upper_bound: # chained comparison. Market price is between lower and upper bound = True
    print("🟡The stock price is fairly valued.") 
else:
    print("🔴 The stock is overvalued. Consider selling.")

# Terminal value 

