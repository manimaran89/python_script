class TestStack():
    def __init__(self, list):
        self.stack = list

    def __str__(self):
        return str(self.stack)

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        if self.stack:
            return False
        return True

ts = TestStack([1,2,3])
print ts
ts.push(4)
print ts
ts.push(2)
print ts
print ts.pop()
print ts
print ts.is_empty()
