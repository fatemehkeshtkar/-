"کوییز سرکلاس"
def nested_loop_example(n):
    p = 0  # مقدار اولیه p
    for i in range(n):
        for j in range(i, n):
            k = p
            print(k)
            print(p)


def F_n_formula(n):
    # محاسبه F(n) = 3/2 * n * (n + 1)
    return 1.5 * n**2 + 1.5 * n