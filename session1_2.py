"تکه برنامه ای بنویسید که دارای تابع پیچیدگی زمانی زیر باشد
def example1(n):
    for i in range(n):
        for j in range(n):
            print(i)
            print(j)
            print(i + j)


def example2(n):
    a = b = c = d = e = 0  # مقادیر اولیه
    for i in range(n - 2):
        a = b
        b = c
        c = d
        d = e


# محاسبه F(n) = 3n**2 + 4n - 8
def F1(n):
    return 3 * n**2 + 4 * n - 8


# محاسبه F(n) = n**2 + n
def F2(n):
    return n**2 + n