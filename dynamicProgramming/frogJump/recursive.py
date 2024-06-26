def minimumEnergy(self, height, n):
    def somfun(height, i):
        if i==0:
            return 0
        left = somfun(height,i-1) + abs(height[i]-height[i-1])
        right = float('inf')
        if i > 1:
            right = somfun(height,i-2) + abs(height[i]-height[i-2])
        return min(left,right)
    return somfun(height,n-1)