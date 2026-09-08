class Solution:
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        fact= n*self.factorial(n-1)
            
        return fact
        