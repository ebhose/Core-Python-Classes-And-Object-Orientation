#!/usr/bin/env python3


class A:
    def func(self):
        return 'A.func'


class B(A):
    def func(self):
        return 'B.func'



class C(A):
    def func(self):
        return 'C.func'


class D(C, B):
    pass
