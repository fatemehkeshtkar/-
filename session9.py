# تابع بازگشتی فیبوناچی
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# مثال استفاده
for i in range(1, 10):
    print(f"fib({i}) =", fib(i))


# ضرب ماتریسی ساده با سه حلقه تودرتو
def matrix_multiply(a, b):
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][k] += a[i][j] * b[j][k]
    return c


# مثال استفاده
a = [[1, 2], [3, 4]]
b = [[2, 0], [1, 2]]
c = matrix_multiply(a, b)
print(c)  # خروجی: [[4, 4], [10, 8]]


# تابع بازگشتی تست
def test(a, b):
    if a > b:
        return a * b
    return test(a, b - 2) + test(a - 1, b - 3) + 6


# مثال استفاده
result = test(3, 7)
print(result)