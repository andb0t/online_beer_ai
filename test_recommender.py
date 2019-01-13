import random
import string

import pandas as pd

import recommender


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def test_order():
    for _ in range(1000):
        i0 = [random.randint(1, 24)]
        i1 = [random.randint(1, 24)]
        n0 = randomword(i0[0])
        n1 = randomword(i1[0])
        print(n0, n1)
        # first
        data = {n0: i0, n1: i1}
        r0 = recommender.recommend(data)
        # second
        data = {n1: i0, n0: i1}
        r1 = recommender.recommend(data)
        # test
        assert r0 == r1


def test_stability():
    i0 = [random.randint(1, 24)]
    i1 = [random.randint(1, 24)]
    for _ in range(1000):
        # first
        data = {'0': i0, '1': i1}
        r0 = recommender.recommend(data)
        # second
        data = {'0': i0, '1': i1}
        r1 = recommender.recommend(data)
        # test
        assert r0 == r1
