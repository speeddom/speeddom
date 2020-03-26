from rply.token import BaseBox

class NUMBER():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
class VAR():
    def __init__(self, left, right):
        self.left = left
        self.right = right
class EXP():
    def __init__(self, left, right):
        self.left = left
        self.right = right
class ABS():
    def __init__(self, left, right):
        self.left = left
        self.right = right
class APP():
    def __init__(self, left, right):
        self.left = left
        self.right = right
class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right
class SUM(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()
