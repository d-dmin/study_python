f = lambda x, y: x + y
print(f(1,4))

f = lambda x: x ** 2
print(f(2))

f = lambda x: x / 2
print(f(3))

print((lambda x: x + 1)(5))



ex = [1,2,3,4,5]
f = lambda x: x ** 2
print(list(map(f,ex)))
print(map(f, ex))

#zip을 쓰지 않고도 가능
ex = [1,2,3,4,5]
f = lambda x, y: x + y
print(list(map(f,ex, ex)))

ex = [1,2,3,4,5]
print(list(map(lambda x: x ** 2 if x % 2 == 0 else x, ex)))
