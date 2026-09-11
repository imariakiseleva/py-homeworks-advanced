class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def check_brackets(sequence):
    stack = Stack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for bracket in sequence:
        if bracket in '([{':
            stack.push(bracket)

        elif bracket in ')]}':
            if stack.is_empty():
                return 'Несбалансированно'

            if stack.pop() != pairs[bracket]:
                return 'Несбалансированно'

    if stack.is_empty():
        return 'Сбалансированно'

    return 'Несбалансированно'


if __name__ == '__main__':
    sequence = input('Введите последовательность скобок: ')
    print(check_brackets(sequence))