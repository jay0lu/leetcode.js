# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in range(0,len(nums)-1):
            for b in range(a,len(nums)):
                added = nums[a] + nums[b]
                if added == target:
                    print(a,b)


    # better solution, using hash table(dir)
    def twoSumHash(nums, target):
        # store list to dir
        D = {}
        for a in range(0,len(nums)):
            D[a] = nums[a]
        # find the value
        for x in range(0,len(nums)):
            target_value = target - nums[x]
            # print(list(D.values()))
            if target_value in D.values():
                # convert dict values to list, find list index
                target_index = list(D.values()).index(target_value)
                print(x,target_index)
                break



nums = [2, 7, 11, 15]
target = 9
print("brute force result:")
Solution.twoSum(nums,target)
print("Dict(hash table) result:")
Solution.twoSumHash(nums,target)
# print(nums[1])
