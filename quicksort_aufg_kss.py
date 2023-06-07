import math
from random import randint


def quicksort(xs):
    if len(xs) <= 1:
        return xs, 0
    pivot = xs[randint(0, len(xs) - 1)]
    smaller_xs, c1 = quicksort([x for x in xs if x < pivot])
    greater_xs, c2 = quicksort([x for x in xs if x > pivot])
    return smaller_xs + [pivot] + greater_xs, c1 + c2 + 2 * len(xs)


# Teste für 5 Verschiene n.
for n in range(200, 400, 40):
    lst = [randint(0, 1000000) for _ in range(n)]
    _, count = quicksort(lst)
    # Wir nutzen hier den Logarithmus zur Basis 2
    nlogn = n * math.log2(n)
    print(f"count: {count}; nlogn: {nlogn}")
