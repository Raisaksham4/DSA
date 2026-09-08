class Solution:
    def armstrongNumber (self, n):
        # code here 
        num=n
        
        num=str(num)
        new=0
        
        for i in range(len(num)):
            new+=(int(num[i]))**3
            i+=1
        
        if new == n:
            return True
        else: return False