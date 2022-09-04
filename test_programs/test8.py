from collections import deque

class Stack:

    def __init__(self):
        self.container = deque()

    def push(self, element):
        self.container.append(element)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(string):
    stack = Stack()
    str = ''
    for letter in string:
        stack.push(letter)
    for _ in range(stack.size()):
        str += stack.pop()
    return str

# print(reverse_string("We will conquere COVID-19"))

def is_balanced(string):
    stack = Stack()
    for letter in string:
        if letter == "(" or letter == "[" or letter == "{":
            stack.push(letter)
        if letter == ")" or letter == "]" or letter == "}":
            if stack.size() == 0:
                return False
            last = stack.peek()
            if (last == "{" and letter == "}") or (last == "(" and letter == ")") or (last == "[" and letter == "]"):
                stack.pop()
    return True if stack.size() == 0 else False


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))


    
