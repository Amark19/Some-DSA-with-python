from bubbleSort import demo##now here __main__ will become dmo2 & demo1 is nothing but one python module so demo1's __name__ will be demo1

obj = demo(10)
print(obj.return_x())
if __name__ == "main":
    print(__name__)
else:
    print(__name__)