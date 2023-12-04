#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 14 вариант
def sqrt(x, k, st=1, eps=1e-4):
    y = st + ((x / st ** (k - 1)) - st) / k
    if abs(st - y) < eps:
        return y
    else:
        return sqrt(x, k, y, eps)


if __name__ == "__main__":
    print(sqrt(8, 3))
