def isValid(s):
    stack = []
    
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif c == '}' and stack and stack[-1] == '{':
            stack.pop()
        elif c == ']' and stack and stack[-1] == '[':
            stack.pop()
        else:
            return False
    
    return len(stack) == 0


# Main part
if __name__ == "__main__":
    input_str = input()
    print(isValid(input_str))
