class Assignment:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __iadd__(self, other):
        return Assignment(self.left + other.left, self.right + other.right)

    def __isub__(self, other):
        return Assignment(self.left - other.left, self.right - other.right)

    def __imul__(self, other):
        return Assignment(self.left * other.left, self.right * other.right)

    def __repr__(self):
        return f"{self.left}j, {abs(self.right)}"


c1 = Assignment(5, 4)
c2 = Assignment(6, 1)
c1 += c2
print(c1)
c1 -= c2
print(c1)
c1 *= c2
print(c1)
