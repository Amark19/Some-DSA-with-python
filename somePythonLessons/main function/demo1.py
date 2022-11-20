## if we are running this script only then interpreter will get to know that somone is trying to run it standalone and not from any other file then it becomes of type '__main__'
class demo:
    def __init__(self,x):
        self.x = x
    def return_x(self):
        return self.x
if __name__ == "__main__":
    obj = demo(8)
    print(obj.return_x())
else:
    print(__name__)