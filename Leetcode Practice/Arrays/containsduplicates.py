class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dict = {}
        # for i, val in enumerate(nums):
        #     if val in dict.values():
        #         return True
        #     else:
        #         dict[i] = val

        # return False
        
        if(len(nums) != len(set(nums))):
            return True
        return False
    