"تابع پیچیدگی تکه برنامه زیر را بنویسید"
def complexity_example(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count  


def F_n_complexity(n):
    import math
    return math.log2(n)  
