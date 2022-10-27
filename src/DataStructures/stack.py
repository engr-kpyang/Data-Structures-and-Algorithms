# Stacks

def create_stack():
    stack = []
    return stack


def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print('Pushed Item: ' + item)


def pop(stack):
    if (check_empty(stack)):
        return 'stack is empty'

    return stack.pop()

Stack = create_stack()
push(Stack, 's')
push(Stack, 't')
push(Stack, 'a')
push(Stack, 'c')
push(Stack, 'k')
push(Stack, str(99))
print(Stack)
pop(Stack)
print(Stack)