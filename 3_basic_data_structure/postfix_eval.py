from stack import Stack

def postfixEval(postfixExpr):
    opStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "+-*/":
            op2 = opStack.pop()
            op1 = opStack.pop()
            result = doMath(token, op1, op2)
            opStack.push(result)
        else:
            opStack.push(int(token))
    
    return opStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval("17 10 + 3 * 9 /"))
