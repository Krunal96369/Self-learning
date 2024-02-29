'''
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.


Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

'''

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        low, high = 1, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low



# Time complexity: O(n log n)

# test case

nums = [1,3,4,2,2]
# Output: 2
print(Solution().findDuplicate(nums))
