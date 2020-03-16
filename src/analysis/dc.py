# -*- coding: utf-8 -*-

# Filename : dc.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
DC Analysis, inherit Analysis
"""

from analysis.base import Analysis


class DCAnalysis(Analysis):
    def __init__(self, atype):
        super(DCAnalysis, self).__init__(atype)

        self.__src1 = None
        self.__start1 = 0
        self.__stop1 = 0
        self.__incr1 = 0
    
    def set_arg1(self, src1, start1, stop1, incr1):
        self.__src1 = src1
        self.__start1 = start1
        self.__stop1 = stop1
        self.__incr1 = incr1
    
    def do_analysis(self):
        pass