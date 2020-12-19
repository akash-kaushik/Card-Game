a = []
b = []
c = []

print(a)

def test_fun(x, y, z):
    x.append("a")
    y.append("b")
    z.append(1)
    x.append(3)
    return

test_fun(a, b, c)
print("After running : ", a, b, c)

a = []
print(type(a))
print("a:", a)