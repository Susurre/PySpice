# -*- coding: utf-8 -*-

# Filename : matrix.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Define Matrix and Vector structure.
Gnd(number = 0) must be at the first row and first column,
Matrix and Vector's size is (n) x (n), (n) x 1.
Matrix is not sparse matrix.
dtype meansing data type, real or complex.
"""

import numpy as np

from define import const


class Matrix():
    def __init__(self, size, dtype):
        self.set_size(size)
        self.set_dtype(dtype)
        
        self.mat = np.zeros((self.__size, self.__size), self.__dtype)
    
    def set_size(self, size):
        size = int(size)
        if size <= 0:
            size = 1
        self.__size = size
    
    def get_size(self):
        return self.__size
    
    def set_dtype(self, dtype):
        if dtype != 'float' and dtype != 'complex':
            self.__dtype = 'complex'
        else:
            self.__dtype = dtype
    
    def get_dtype(self):
        return self.__dtype
    
    def set_value(self, row, col, value):
        assert 0 <= row < self.__size
        assert 0 <= col < self.__size

        self.mat[row, col] = value

    def add_value(self, row, col, value):
        assert 0 <= row < self.__size
        assert 0 <= col < self.__size

        self.mat[row, col] += value

    def get_value(self, row, col):
        assert 0 <= row < self.__size
        assert 0 <= col < self.__size

        return self.mat[row, col]

    """
    Set all elements to zero.
    """
    def clear(self):
        if self.__dtype == 'float':
            self.mat[:] = 0
        elif self.__dtype == 'complex':
            self.mat[:] = 0 + 0j

    def print_to_screen(self):
        if self.__dtype == 'float':
            width = const.PRINT_FLOAT_WIDTH
        else:
            width = const.PRINT_COMPLEX_WIDTH

        print("Modified Nodal Matrix")

        # The first line
        line = "{0:<{1}s}".format("index", width)
        for i in range(self.__size):
            line += "{0:<{1}d}".format(i, width)
        print(line)

        # Print every row.
        for i in range(self.__size):
            line = "{0:<{1}d}".format(i, width)
            for j in range(self.__size):
                if self.__dtype == 'float':
                    line += "{0:<{1}.2f}".format(self.get_value(i, j), width)
                else:
                    line += "{0.real:<{1}.2f}{0.imag:<{1}.2f}j".format(self.get_value(i, j), width)
            print(line)

    def dump_to_file(self):
        pass

class Vector():
    def __init__(self, size, dtype):
        self.set_size(size)
        self.set_dtype(dtype)
        
        self.vec = np.zeros((self.__size, 1), self.__dtype)
        self.vec[0, 0] = 0
    
    def set_size(self, size):
        size = int(size)
        if size <= 0:
            size = 1
        self.__size = size
    
    def get_size(self):
        return self.__size
    
    def set_dtype(self, dtype):
        if dtype != 'float' and dtype != 'complex':
            self.__dtype = 'complex'
        else:
            self.__dtype = dtype
    
    def get_dtype(self):
        return self.__dtype
    
    def set_value(self, row, value):
        assert 0 <= row < self.__size

        self.vec[row, 0] = value

    def add_value(self, row, value):
        assert 0 <= row < self.__size

        self.vec[row, 0] += value

    def get_value(self, row):
        assert 0 <= row < self.__size

        return self.vec[row, 0]

    """
    Set all elements to zero.
    """
    def clear(self):
        if self.__dtype == 'float':
            self.vec[:] = 0
        elif self.__dtype == 'complex':
            self.vec[:] = 0 + 0j
    
    def print_to_screen(self):
        if self.__dtype == 'float':
            width = const.PRINT_FLOAT_WIDTH
        else:
            width = const.PRINT_COMPLEX_WIDTH
        
        print("Right Hand Side")

        # The first line.
        line = "{0:<{1}s}".format("index", width)
        line += "{0:<{1}d}".format(0, width)
        print(line)
        
        # Print every row.
        for i in range(self.__size):
            line = "{0:<{1}d}".format(i, width)
            if self.__dtype == 'float':
                line += "{0:<{1}.2f}".format(self.get_value(i), width)
            else:
                line += "{0.real:<{1}.2f}{0.imag:<{1}.2f}j".format(self.get_value(i), width)
            print(line)
            
    def dump_to_file(self):
        pass