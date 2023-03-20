class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __str__ (self):
        return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'
myObject = MyClass(12345, "Hello")


print(myObject)#if we don't have __str__ then it prints refernce of object & its address but if we have __str__ then it prints whatever in the __str__ method(string form of object)
print(str(myObject))
print(myObject.__repr__())
