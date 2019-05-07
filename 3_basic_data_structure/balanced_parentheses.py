'''
使用stack作為核對小括號的實作方式
'''
from stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        
        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker("((()))"))
print(parChecker("((())"))