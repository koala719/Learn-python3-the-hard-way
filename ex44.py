# Implicit inheritance
class ParentA(object):

    def implicit(self):
        print("PARENT implicit()")

class ChildA(ParentA):
    pass

dad_a = ParentA()
son_a = ChildA()

dad_a.implicit()
son_a.implicit()

# Explicit coverage
class ParentB(object):

    def override(self):
        print("PARENT override()")

class ChildB(ParentB):

    def override(self):
        print("CHILD override()")

dad_b = ParentB()
son_b = ChildB()

dad_b.override()
son_b.override()

# Replace before or after operation
class ParentC(object):

    def altered(self):
        print("PARENT altered()")

class ChildC(ParentC):

    def altered(self):
        print("CHILD, BERORE PARENT altered()")
        super(ChildC, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad_c = ParentC()
son_c = ChildC()

dad_c.altered()
son_c.altered()

# combination
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BERORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

# hmmmmmmmmmm
class Other(object):

    def implicit(self):
        print("OTHER implicit()")

    def override(self):
        print("OTHER override()")

    def altered(self):
        print("OTHER altered()")

class ChildD(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BERORE PARENT altered()")
        self.other.altered()
        print("CHILD, AFTER PARENT altered()")

son_d = ChildD()

son_d.implicit()
son_d.override()
son_d.altered()
