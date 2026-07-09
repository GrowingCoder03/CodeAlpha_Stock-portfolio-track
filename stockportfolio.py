stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 150,
    "MSFT": 320
}

total_investment = 0

print("Available Stocks:")
for stock in stock_prices:
    print(stock, ":", stock_prices[stock])

n = int(input("\nEnter number of different stocks you have: "))

for i in range(n):
    stock_name = input("\nEnter Stock Name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter Quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment in", stock_name, "=", investment)

    else:
        print("Stock not available.")

print("\nTotal Investment =", total_investment)

