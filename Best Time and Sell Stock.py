class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initalize two pointer: 
        l = 0   #left = buy (day 0)
        r = 1   #right = sell (day 1)
        
        #keep track of the maximum profit found so far
        maxprofit = 0

        #loop until the 'sell' pointer reaches the end of the price list
        while r < len(prices):
            
            #Check if buying at l and selling at r is profitable 
            if prices[l] < prices[r]:               #is it profitable
            
            #calculate the profit if its a profitable 
                profit  = prices[r] - prices[l]
                
                #update the maxprofit with the higher value between current maxprofit and new profit
                maxprofit = max(maxprofit, profit)
                
            else:
                #if buying at l and selling at r is not profitable, 
                #move the 'buy' pointer to the current 'sell' pointer
                l = r 
                
            #move the 'sell' pointer one day forward
            r +=1
        
        #Return max profit after check all possiblility 
        return maxprofit
