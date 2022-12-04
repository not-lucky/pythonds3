class Stack:

    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return not bool(len(self.items))

    def push(self, ele):
        self.items.append(ele)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def rev_string(my_str):
    a = Stack()
    for i in my_str:
        a.push(i)
    uwu = ""
    for i in range(a.size()):
        uwu += a.pop()
    return uwu


print(rev_string("apple"))