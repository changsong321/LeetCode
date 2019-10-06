def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    mapping = {']': '[', ')': '(', '}': '{'}
    stack = []
    for char in s:
        if char in list(mapping.keys()):
            top = stack.pop() if stack else '*'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

print(isValid("()[]{}"))

