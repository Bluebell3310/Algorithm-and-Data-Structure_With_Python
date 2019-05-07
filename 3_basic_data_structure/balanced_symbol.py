'''
使用stack作為核對大中小括號的實作方式
'''
from stack import Stack

def symChecker(symbolString):
    s = Stack()
    balenced = True
    index = 0
    while index < len(symbolString) and balenced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balenced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balenced = False    
        index += 1
    if balenced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(symChecker("{[][]"))
print(symChecker("{()[]{}}"))
