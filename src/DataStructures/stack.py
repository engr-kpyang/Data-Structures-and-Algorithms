# Stack Data Structure

def create_stack():
    stack = []
    return stack

def stack_peek(stack):
        top = stack[-1]
        return f'The current element on top is: {top}'   

def push(stack, item):
    stack.append(item)
    print(f"Pushed item '{item}', into the stack.")


def pop(stack):
    if len(stack) == 0:
        return 'stack is empty'
        
    return stack.pop()


stack = create_stack()
push(stack, 's')
print(stack)
push(stack, 't')
print(stack)
push(stack, 'a')
print(stack_peek(stack))
push(stack, 'c')
push(stack, 'k')
push(stack, str(99))
print(stack)
pop(stack)
pop(stack)
print(stack)


