'''

You are given an array/list 'prices' where the elements of the array represent the prices of the stock as they were 
yesterday and indices of the array represent minutes. 
Your task is to find and return the maximum profit you can make by buying and selling the stock.
You can buy and sell the stock only once.

Note:
You can’t sell without buying first.
For Example:
For the given array [ 2, 100, 150, 120],
The maximum profit can be achieved by buying the stock at minute 0 when its price is Rs. 2 and selling it at minute 2 when its price is Rs. 150.
So, the output will be 148.
'''
def array_input():
    user_input = input("Enter space-separated integers: ")
    array=[int(x) for x in user_input.split()]
    return array

def profit_calculation(user_data):
    if not user_data or len(user_data) < 2:
        print("The data are not Fully loaded",0)
    else:
        min_price=user_data[0]
        max_profit=0
        for i in user_data[1:]:
            min_price=min(min_price,i)
            max_profit=max(max_profit,i-min_price)
        return max_profit

profit_by_min=array_input()
print("The max profit is the",profit_calculation(profit_by_min))
