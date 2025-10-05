def createstack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isempty(stack):
    if size(stack) == 0:
        return True
    else:
        return False

def push(stack,item):
    stack.append(item)

def pop(stack):
    if isempty(stack):
        return
    return stack.pop()

def reversestr_usingstack(str):
    stack = createstack()
    reversedstring = ""

    len_of_string = len(str)

    for i in range(0,len_of_string,1):
        push(stack,str[i])

    for i in range(0,len_of_string,1):
        reversedstring = reversedstring + pop(stack)

    return reversedstring
