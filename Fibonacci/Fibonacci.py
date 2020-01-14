# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# Matrix power with modulos 
# Source: https://stackoverflow.com/a/26284607
from numpy.core.numeric import concatenate, isscalar, binary_repr, identity, asanyarray, dot
from numpy.core.numerictypes import issubdtype    
def matrix_power(M, n, mod_val):
    # Implementation shadows numpy's matrix_power, but with modulo included
    M = asanyarray(M)
    if len(M.shape) != 2 or M.shape[0] != M.shape[1]:
        raise ValueError("input  must be a square array")
    #if not issubdtype(type(n), int):
    #    raise TypeError("exponent must be an integer")

    from numpy.linalg import inv

    if n==0:
        M = M.copy()
        M[:] = identity(M.shape[0])
        return M
    elif n<0:
        M = inv(M)
        n *= -1

    result = M % mod_val
    if n <= 3:
        for _ in range(n-1):
            result = dot(result, M) % mod_val
        return result

    # binary decompositon to reduce the number of matrix
    # multiplications for n > 3
    beta = binary_repr(n)
    Z, q, t = M, 0, len(beta)
    while beta[t-q-1] == '0':
        Z = dot(Z, Z) % mod_val
        q += 1
    result = Z
    for k in range(q+1, t):
        Z = dot(Z, Z) % mod_val
        if beta[t-k-1] == '1':
            result = dot(result, Z) % mod_val
    return result % mod_val

from numpy import array
def fibonacci(n):
    F = array([[1, 1], [1, 0]])
    return matrix_power(F, n, 10)[0, 1]

n = get_number()
for _ in range(n):
    t = get_number()
    print(fibonacci(t + 1))
