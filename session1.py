"تابع پیچیدگی زمانی الگوریتم زیر را محاسبه کنید"
def compute(n):
    a = 5
    l = 0
    t = 0

    for i in range(n):
        p = t
        t = l + 6
        l += 2

    return a, l, t
    