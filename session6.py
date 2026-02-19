def example_complexity(n):
    # حلقه اول: i از 0 تا n-1
    for i in range(n):
        # حلقه دوم: j از 0 تا n-1 با گام 3
        for j in range(0, n, 3):
            a = i + j
            b = i - j
            c = i * j
            d = (i + j) % 2
        e = i**2
        f = i + 5
        g = i - 3
        h = 2 * i
        k = i // 2

    # حلقه سوم: i از 0 تا n-1 با گام 3
    for i in range(0, n, 3):
        # حلقه داخلی: j از -1 تا n-1 با گام 3
        for j in range(-1, n, 3):
            x = i + j
            y = i - j
        m = i * 2
        n_val = i + 7
        p = i - 1

    # حاصل تقریبی تابع پیچیدگی: F(n) ~ 1.3*n**2 + 6*n + 2
    F_n = 1.3 * n**2 + 6 * n + 2
    return F_n


# مثال استفاده
n = 10
print("F(n) ≈", example_complexity(n))