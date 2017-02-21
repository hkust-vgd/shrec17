from __future__ import division
import math
import numpy as np

# More details about evaluation metrics can be found here
# https://arxiv.org/pdf/1105.3685.pdf


def precision(x):
    return np.count_nonzero(x) / len(x)


def recall(x, freq):
    return np.count_nonzero(x) / freq


def f1score(x, freq):
    p = precision(x)
    r = recall(x, freq)
    if p + r == 0.0:
        return 0.0
    return 2 * p * r / (p + r)


def average_precision(x, freq):
    dr = 1.0 / freq # change in recall
    tp = 0
    ap = 0.0
    for k, _ in enumerate(x):
        if x[k]:
            tp += 1
            ap += (tp / (k + 1))
    return ap * dr


def dcg(x):
    total = x[0]
    for i, _ in enumerate(x[1:]):
        w = 1.0 / math.log(i + 2, 2)
        total += x[i] * w
    return total


def idcg(x):
    return dcg(sorted(x, reverse=True))


def ndcg(x):
    i = idcg(x)
    if i == 0.0:
        return 0.0
    return dcg(x) / i


def nnt1(x, k):
    return np.count_nonzero(x[:k]) / k


def nnt2(x, k):
    k2 = min(len(x), k*2)
    return np.count_nonzero(x[:k2]) / (k2)
