class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        arr = [amount + 1] * (amount + 1)
        arr[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    """
                    if i - coin is an actual value, we know that "coin"
                    can represent 1 coin, and the rest of it is an accumulation
                    of the min of the currval (i) - coin. 
                    We do that and the min of arr[i], because we need to go through
                    every possible coin, and see if we can reduce the number
                    """
                    arr[i] = min(arr[i], arr[i - coin] + 1)

        if arr[amount] <= amount:
            return arr[amount]
        return -1
