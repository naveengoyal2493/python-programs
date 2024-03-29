"""
Given a value V, if we want to make a change for V cents, and we have an infinite 
supply of each of C = { C1, C2, .., Cm} valued coins, what is the minimum number of 
coins to make the change? If it’s not possible to make a change, print -1.

Examples:  

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required We can use one coin of 25 cents and one of 5 cents 

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required We can use one coin of 6 cents and 1 coin of 5 cents
"""

def find_minimum_coins(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if (a - c) >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    
    return dp[amount] if dp[amount] != amount + 1 else -1

coins = [25, 10, 5]
amount = 30
print(find_minimum_coins(coins, amount))