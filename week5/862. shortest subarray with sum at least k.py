import collections
def shortestSubarray(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    if sum(A) < K:
        return -1
    length = 1000000
    q = collections.deque()
    q.append(A[0])w
    if sum(q) >= K and sum(q) < length:
        length = sum(q)
    else:

    '''else:
        length = 10000000000
        for i in range(len(A)):
            q = collections.deque()
            q.append(A[i])
            for j in range(i+1,len(A)):
                if sum(q) >= K and len(q) < length:
                    length = len(q)
                else:
                    q.append(A[j])
        return length'''
A=[1,2]
K=7
print(shortestSubarray(A, K))