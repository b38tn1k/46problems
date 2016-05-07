# RUSSIAN PEASANT ALGORITHIM
# multiply large numbers together through doubling, halving and adding


def russian(val1, val2):
    solution = 0
    while not val1 == 1:
        val1 = val1 >> 1    # val1 = val1 / 2
        val2 = val2 << 1    # val2 = val2 * 2
        if val1 % 2 == 1: solution += val2
    print(solution)

russian(68, 32)
russian(32, 68)
russian(7852, 460)
