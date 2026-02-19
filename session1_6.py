"تکه برنامه ای بنویسید که دارای تابع پیچیدگی زمانی زیر باشد"
def loop_pattern1(n):
    for i in range(n):
        for j in range(0, n, 3):
            # هر نقطه چین یک دستور است
            a = i + j
            b = i - j
            c = i * j
            d = j - i
        e = i**2
        f = i + 2
        g = i - 2
        h = 2 * i
        i_val = i // 2
        j_val = i % 2


def loop_pattern2(n):
    for i in range(0, n, 3):
        for j in range(-1, n, 3):
            a = i + j
            b = i - j
        c = i**2
        d = i * 2
        e = i + 5
        f = i - 5

# محاسبه تقریبی F(n) = 2/9 * n**2 + 14/9 * n
def F_n_student(n):
    return 2/9 * n**2 + 14/9 * n


# محاسبه F(n) = 1.3*n**2 + 6*n + 2 (نمونه دیگر)
def F_n_example(n):
    return 1.3 * n**2 + 6 * n + 2