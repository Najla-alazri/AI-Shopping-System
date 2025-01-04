def calculate_total(prices):
    """
    Calculate the total price of a list of items.
    """
    total = 0
    for price in prices:
    
        total += price 
    return total

if __name__ == "__main__":
   
    item_prices = [10, 20, -5, 15]

    total_price = calculate_total(item_prices)
    print(f"The total price is: {total_price}")
