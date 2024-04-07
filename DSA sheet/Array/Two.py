'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 
'''

def price(array):
    if not array or len(array)< 2:
        return 0
    min_price=array[0]
    max_profit=0
    for i in array[1:]:
        min_price=min(min_price,i)
        max_profit=max(max_profit,i-min_price)
    return max_profit
        
def input_array():
    array=input("Enter the array:")
    array_input=list(map(int,array.split()))
    return array_input
stocks=input_array()
print("maximum profit is ",price(stocks))
