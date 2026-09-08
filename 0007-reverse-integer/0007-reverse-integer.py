class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if int(x)<0:
            num = int((x[0])+x[1:][::-1])
        else:
            num = int(x[::-1])
        
        if ((-(2**31)) > num or num > ((2**31)-1)):
            return 0
        else: return num
        