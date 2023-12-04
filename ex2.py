#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from timeit import timeit


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if (f.f_back and f.f_back.f_back and
                f.f_back.f_back.f_code == f.f_code):
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def factorial(n, acc=1):
    """calculate a factorial"""
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)


@tail_call_optimized
def fib(i, current=0, nxt=1):
    if i == 0:
        return current
    else:
        return fib(i - 1, nxt, current + nxt)
    
    
if __name__ == '__main__':
    fact_setup = """from __main__ import factorial"""
    fib_setup = """from __main__ import fib"""
    fact_time = timeit(setup=fact_setup, stmt="factorial(50)", number=10)
    fib_time = timeit(setup=fib_setup, stmt="fib(20)", number=10)

    print(f"Время выполнения функции factorial: {fact_time}")
    print(f"Время выполнения функции fib: {fib_time}")