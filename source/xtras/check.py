def check():
    for i in range(2):
        yield i


# x = check()
# print(x)
# print(next(x))
# print(next(x))


x = [1, 2, 3]

while x:
    print("p")
    x.pop()
