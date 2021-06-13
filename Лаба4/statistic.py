import numpy as np
from math import ceil, log2


def avg(list):
    return np.mean(list)


def dispersion(list):
    res = 0
    for i in list:
        res += (i - np.mean(list)) ** 2
    return res / len(list)


def variation_coefficient(list):
    return (dispersion(list) ** (1/2) / np.mean(list)) * 100


def chi_square(list):
    b = sorted(list)
    k = ceil(log2(len(list)) + 1)
    step = 10000 / k
    p = 1 / k

    frequency_vector = []

    for i in range(k):
        counter = 0
        for j in b:
            if (j > i * step) and (j <= (i + 1) * step):
                counter += 1
            else:
                continue
        frequency_vector.append(counter)
    chi = 0
    for i in range(k):
        chi += ((frequency_vector[i] - p * len(list)) ** 2) / (p * len(list))

    return 0.8 <= chi <= 16.8
