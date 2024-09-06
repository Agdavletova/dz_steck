class Stack:
    def __init__(self):
        self.stack = []
        self.num = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num >= len(self.stack):
            raise StopIteration
        else:
            return self.stack[self.num]

    def __len__(self) -> int:
        return len(self.stack)

    def is_empty(self)-> bool:
        return not len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop(len(self.stack) -1)

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)



def convert_str_stack(s:str) -> Stack:
    stack = Stack()
    for i in s:
        stack.push(i)
    return stack

def balance_test(s:str) -> str:
    stack = convert_str_stack(s)
    k = len(stack)
    unique_parentheses = {
             "()": 0,
             "[]": 0,
             "{}": 0
         }
    for i in range(k):
        symbol = stack.pop()
        if symbol == "(" or symbol == ")":
            if unique_parentheses["()"] < 2:
                unique_parentheses["()"] += 1
            else:
                unique_parentheses["()"] = 1
        elif symbol == "{" or symbol == "}":
            if unique_parentheses["{}"] < 2:
                unique_parentheses["{}"] += 1
            else:
                unique_parentheses["{}"] = 1
        elif symbol == "[" or symbol == "]":
            if unique_parentheses["[]"] < 2:
                unique_parentheses["[]"] += 1
            else:
                unique_parentheses["[]"] = 1
    if 1 in unique_parentheses.values():
        result = "Несбалансированно"
    else:
        result = "Сбалансированно"
    return result


print(balance_test("((())){{}}]["))
