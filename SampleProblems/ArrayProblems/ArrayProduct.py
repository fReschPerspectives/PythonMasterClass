"""
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums 
except nums[i].

The product of any prefix or suffix of nums is guaranteed to 
fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without 
using the division operation.
"""
import numpy as np

class Solution:
    def productExceptSelf(nums: list[int]) -> list[int]:
        output = []  

        for i in range(len(nums)):
            work = np.array(nums)
            output.append(np.delete(work, i).prod())
            
        return output

nums = [1,2,3,4]
nums2 = [-1,1,0,-3,3]
print(Solution.productExceptSelf(nums=nums))
print(Solution.productExceptSelf(nums=nums2))