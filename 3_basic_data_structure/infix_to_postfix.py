from stack import Stack

def infixToPostfix(infixexpr):
    prec = {}  # prec = precedence
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "()+-*/": 
            if token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(opStack.pop())
                opStack.push(token)
        else:
            postfixList.append(token)
            
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    return " ".join(postfixList)

print(infixToPostfix("10 + 3 * 5 / ( 16 - 4 )"))