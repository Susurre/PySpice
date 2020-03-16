# -*- coding: utf-8 -*-

# Filename : solver.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Solve Ax = B, return x
A : Matrix
x : Vector
B : Vector
"""

from maths.sparse.matrix import Matrix, Vector

import numpy as np


class Solver():
    def __init__(self, A, B):
        isinstance(A, Matrix)
        isinstance(B, Vector)

        assert A.get_size() == B.get_size()

        self.__A = A
        self.__B = B

    def set_A(self, A):
        isinstance(A, Matrix)

        self.__A = A
    
    def set_B(self, B):
        isinstance(B, Vector)

        self.__B = B

    """
    The first row and col is invalid of Matrix.
    The first row is invalid of Vector.
    """
    def solve(self):
        assert self.__A.get_size() == self.__B.get_size()
        size = self.__A.get_size()

        A = self.__A.mat[1:, 1:]
        B = self.__B.vec[1:, 1:]

        x = np.linalg.solve(A, B)

        solution = Vector(size, self.__A.get_dtype())

        for i in range(size - 2):
            solution.set_value(i + 1, x[i, 0])

        return solution

