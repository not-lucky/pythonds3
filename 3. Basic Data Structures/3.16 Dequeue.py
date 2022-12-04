class Dequeue():

    def __init__(self) -> None:
        self.item = []

    def add_front(self, ele):
        self.item.insert(0, ele)

    def add_rear(self, ele):
        self.item.append(ele)

    def remove_front(self):
        return self.item.pop(0)

    def remove_rear(self):
        return self.item.pop()

    def is_empty(self):
        return not bool(len(self.item))

    def size(self):
        return len(self.item)


d = Dequeue()
pal = True

for i in input():
    d.add_rear(i)

for i in range(d.size() // 2):
    front = d.remove_front()
    rear = d.remove_rear()
    if front != rear:
        print("Not a palindrome.")
        pal = False
        break

if pal:
    print("Palindrome.")