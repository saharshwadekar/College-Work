def maxProfit(prices: list[int]) -> int:
  p = sorted(prices)
  length = len(prices) // 2
  l, b = 0, -1
  while(length):
    length -= 1
    l = prices.index(p[l])
    b = prices.index(p[b])
    if l < b:
      return prices[l] - prices[b]
    
  return 0
  
  

prices = [7,1,5,3,6,4]
# print(prices.find(min(prices)))
print(maxProfit(prices))