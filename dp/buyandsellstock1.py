def solution(prices):

    profit = 0 
    curr_min =  0 

    for sale in prices:
        curr_profit = sale - prices
        profit = max(profit,curr_profit)
        curr_min = min(curr_min,sale)
    return profit

