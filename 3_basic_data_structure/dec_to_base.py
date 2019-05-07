'''
此程式將時進位轉為16進位(含)以下任何一進位
'''
from stack import Stack

def baseConverter(decNumber, base):
    digit = "0123456789ABCDEF"

    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    
    newString = ""
    while not remstack.isEmpty():
        newString = newString + digit[remstack.pop()]
    
    return newString

print(baseConverter(42, 16))