class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        for i,n in enumerate(nums):
            recur_permute = self.permute(nums[:i] + nums[i+1:])
            for item in recur_permute:
                res.append([n]+item)
        return res

test = Solution()
nums = [1,2,3,4]
print(test.permute(nums))