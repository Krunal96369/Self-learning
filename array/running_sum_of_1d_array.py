'''
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

Example 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]

Example 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]

Constraints:
    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6

'''

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# Time complexity: O(n)

# Space complexity: O(1) as we are not using any extra space

# Approach: We are using the same array to store the running sum. We are iterating through the array and adding the previous element to the current element.

# We are not using any extra space, so the space complexity is O(1). The time complexity is O(n) as we are iterating through the array once.


# test the solution

# s = Solution()
# print(s.runningSum([1,2,3,4])) # [1,3,6,10]
# print(s.runningSum([1,1,1,1,1])) # [1,2,3,4,5]
