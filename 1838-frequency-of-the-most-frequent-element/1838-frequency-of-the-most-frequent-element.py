class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        max_freq=0

        for right in range(len(nums)):
            target=nums[right]
            window_sum += nums[right]
            
            while target * (right-left+1) - window_sum > k:
                window_sum -= nums[left]
                left += 1

                cost = nums[right] * (right-left+1) - window_sum
            
            max_freq = max(max_freq, right-left + 1)
        return max_freq

            
        
        
        