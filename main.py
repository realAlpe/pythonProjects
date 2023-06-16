from random import choice


def wuerfe(n: int) -> float:
    # n ist anzahl der muenzwuerfe
    return sum(choice([0, 1]) for _ in range(n)) / n


def durchlauf(m: int, n: int) -> float:
    # m ist anzahl der experiment, n ist anzahl der muenzwuerfe
    return sum(1 for _ in range(m) if 0.49 < wuerfe(n) < 0.51) / m


def main():
    k = []
    for _ in range(20):
        prob = durchlauf(100, 15626)
        # print(prob)
        k.append(prob)
    print(k)


if __name__ == '__main__':
    main()  #
