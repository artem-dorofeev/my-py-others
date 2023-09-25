# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pass

class Solution(object):
    def twoSum(self, nums, target):
        print(nums, target)
        nums2 = nums[::]

        # for item in nums2:
            
        #     test_list = nums2[1::]
        #     test_nums = item

        #     for i in test_list:
        #         if test_nums + i == target:
        #             print(f"OK  {test_nums} + {i}")

        #     nums2 = nums2[1::]
        
        # a = len(nums)
        check = 1
        i = 0

        while i < len(nums):
            test_list = nums[check::]

            n = 0
            while n < len(test_list):
                if nums[i] + test_list[n] == target:
                    print(f"OK  {nums[i]} + {test_list[n]}  ({i}, {n + check})")
                    result = [i, n + check]
                    return result
                n += 1

            check += 1
            i += 1


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result_list = []

    
if __name__ == "__main__":
    # print(main())
    nums1 = [6,2,7,11,15]
    target1 = 17
    test_obj = Solution()
    print(test_obj)
    result = test_obj.twoSum(nums1, target1)
    print(type(result))


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?"""