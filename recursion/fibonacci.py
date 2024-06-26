def fibonacci(num, a, b):
    if num == 0:
        return b
    temp = a + b
    a = b
    b = temp
    return fibonacci(num-1, a, b)


def fibonacci2(num):
    if num <= 1:
        return num
    return fibonacci2(num-1) + fibonacci2(num-2)


# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
print(fibonacci(5, 0, 1))#2^n
print(fibonacci2(5))#O(N)


5

a = 1
b= 1
sum = 0

# 1 1 2 3 5 8

5
4
35
2 + 0


