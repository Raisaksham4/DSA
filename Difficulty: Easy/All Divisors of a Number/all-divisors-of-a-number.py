class Solution:
    def getDivisors(self, n):
        
        arr=[]

        for i in range(1, (int(n**0.5)) + 1):
            if n % i == 0:
                arr.append(i)
                if i!= n//i:
                    arr.append(n//i)
                
        return sorted(arr)