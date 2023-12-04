#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timeit import timeit
from functools import lru_cache


@lru_cache
def factorial_rec(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


def factorial_iter(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


@lru_cache
def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 2) + fib_rec(n - 1)


def fib_iter(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == "__main__":
    fact_rec_setup = """from __main__ import factorial_rec"""
    fact_iter_setup = """from __main__ import factorial_iter"""
    fact_rec_time = timeit(setup=fact_rec_setup, stmt="factorial_rec(50)", number=10)
    fact_iter_time = timeit(setup=fact_iter_setup, stmt="factorial_iter(50)", number=10)

    fib_rec_setup = """from __main__ import fib_rec"""
    fib_iter_setup = """from __main__ import fib_iter"""
    fib_rec_time = timeit(setup=fib_rec_setup, stmt="fib_rec(30)", number=10)
    fib_iter_time = timeit(setup=fib_iter_setup, stmt="fib_iter(30)", number=10)

    print("Функция факториала:")
    print(f"Время выполнения рекурсивной функции {fact_rec_time}")
    print(f"Время выполнения итеративной функции {fact_iter_time}\n")

    print("Функция чисел Фибоначчи:")
    print(f"Время выполнения рекурсивной функции {fib_rec_time}")
    print(f"Время выполнения итеративной функции {fib_iter_time}")
