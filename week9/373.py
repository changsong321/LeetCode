import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k) :
        n = len(nums1)
        m = len(nums2)
        if n == 0 or m == 0:
            return []
        heap = []
        ans = []
        ind = [0] * n
        for i in range(n):
            heapq.heappush(heap, (nums1[i]+nums2[ind[i]],i)) # 给nums1的所有数都加上nums2的第一个数
        while k > 0 and n > 0:
            x = heap[0][1] # 和最小的
            ans.append([nums1[x],nums2[ind[x]]])
            heapq.heappop(heap)
            ind[x] += 1 # 去加nums2的下一个数
            if ind[x] < m: # 当nums2里还有数时，将当前nums1里最小的数和nums2里下一个数相加，放到栈里
                heapq.heappush(heap, (nums1[x]+nums2[ind[x]],x))
            else:
                n -= 1
            k -= 1
        return ans

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
test = Solution()
print(test.kSmallestPairs(nums1,nums2,k))