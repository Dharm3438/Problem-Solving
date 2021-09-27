'''
2012. Sum of Beauty in the Array

You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
0, if none of the previous conditions holds.
Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.
'''

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        sumi = 0
    
        maxi=[0]*len(nums)
        maxi[0] = nums[0]
        for i in range(1,len(nums)):
            if(maxi[i-1]<nums[i-1]):
                maxi[i] = nums[i-1]
            else:
                maxi[i] = maxi[i-1]
        
        # Fill left array
        n = len(nums)
        left = [0]*len(nums)
        right = [0]*len(nums)
    
        left[0] = nums[0]
        for i in range( 1, n):
            left[i] = max(left[i-1], nums[i])
     
        # Fill right array
        right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right[i] = min(right[i + 1], nums[i]);
    
        #for i in range(1,len(nums)):
        #    if(mini[i-1]>nums[i]):
        #        mini[i] = nums[i]
        #    else:
        #        mini[i] = mini[i-1]
        
        #print(maxi)
        #print(left)
        #print(right)
        #print(nums)
    
        for i in range(1,len(nums)-1):
            #val1 = max(nums[:i])
            #val2 = min(nums[i+1:])
            #print(val1,val2,nums[i])
            if(maxi[i]<nums[i] and nums[i]<right[i+1]):
                sumi+=2
            elif(nums[i-1]<nums[i] and nums[i]<nums[i+1]):
                sumi+=1
            
        return sumi