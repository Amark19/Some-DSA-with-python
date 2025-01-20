x = int(input())


def sqrt(x):
    s, e = 0, x
    while s + 1 < e:
        mid = (s + e) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            s = mid
        else:
            e = mid
    if e * e == x: return e
    return s


print(sqrt(x))
