class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique=set(nums)
        unique = sorted(unique, reverse=True)

        if len(unique)>=3:
            return unique[2]
        return unique[0]
    
