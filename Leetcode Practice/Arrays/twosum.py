class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {} # initialize dict, key is index, val is difference
        for i in range(0, len(nums)):
            curr = target - nums[i]
            if nums[i] in dict.values():
                # if difference exists as a value, we've seen it before, so return indices
                return [i, [k for k, v in dict.items() if v == nums[i]][0]]
            
            else:
                dict[i] = curr
        return

        """
        Cleaner Solution
        """
        # dict={}
        # for i,n in enumerate(nums):
        #     print(i, n)
        #     if n in dict:
        #         return dict[n],i
        #     else:
        #         dict[target-n]=i