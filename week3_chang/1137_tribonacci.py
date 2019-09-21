def tribonacci(n):
    """
    :type n: int
    :rtype: int
    """
    a, b, c = 0, 1, 1
    for i in range(n):
        a, b, c = b, c, a + b + c
    return a

print(tribonacci(5))