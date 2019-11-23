class Solution:
    def eraseOverlapIntervals(self, intervals) :
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key = lambda x:x[1])
        last = intervals[0][0] # 记录不断往右推的右端点
        for item in intervals:
            if last <= item[0]: # 该区间的左端点>目前右端点的界限，则它们不重叠，不删
                n -= 1
                last = item[1]
        return n

test = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(test.eraseOverlapIntervals(intervals))