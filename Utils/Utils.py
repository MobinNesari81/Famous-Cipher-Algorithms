import random


def Miller_Rabin_Test(n, k=5):
    """
    Miller-Rabin primality test.
    :param n: integer to check for primality
    :param k: number of iterations (higher value means higher confidence)
    :return: True if n is probably prime, False otherwise
    """

    # Handle small integers
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True

    # Write n - 1 as 2^r * d where d is odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True
