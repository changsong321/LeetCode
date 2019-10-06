def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    stack = []
    path = path.split('/')
    for item in path:
        if item == '..':
            if stack:
                stack.pop()
        elif item and item != '.':
            stack.append(item)
    return '/'+'/'.join(stack)