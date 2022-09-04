def pow(x, n):
    if n == 0: return 1
    if x == 0: return 0
    even_pow = pow(x * x, n // 2)
    return even_pow * x if n % 2 != 0 else even_pow

def helper(x, n):
    res = pow(x, abs(n))
    return res if n >= 0 else 1/res

n = 10
x = 2
print(helper(2,-10))