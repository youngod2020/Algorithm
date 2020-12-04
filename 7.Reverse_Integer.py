class Solution(object):
    def reverse(self, x):
        if x > 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
        elif x < 0:
            x = str(x)[1:]
            x = '-'+x[::-1]
            x = int(x)
        elif x == 0:
            x = 0

        max_result = pow(2, 31)
        if (-max_result < x < max_result - 1):
            return x
        else:
            return 0