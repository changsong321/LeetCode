class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        list = [i for i in range(1,n+1)]
        if k <= 0 or n <= 0 or k>n:
            return [[]]
        elif k == 1:
            return [[i] for i in range(1,n+1)]
        res = []
        for i in list:
            for j in self.combine(n,k-1):
                if [i]+j == sorted([i]+j) and len([i]+j) == len(set([i]+j)):
                    res.append([i]+j)
        return res

test = Solution()
print(test.combine(4,2))