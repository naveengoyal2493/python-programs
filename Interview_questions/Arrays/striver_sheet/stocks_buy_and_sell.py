def stocks_buy_and_sell(prices):
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    
    return max_profit

print(stocks_buy_and_sell([7,1,5,3,6,4]))