# -*- coding: utf-8 -*-

# Filename : ac.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
AC Analysis, inherit Analysis
vtype  : variation type.
points : points per decade/octave.
"""

from analysis.base import Analysis


class ACAnalysis(Analysis):
    def __init__(self, atype):
        super(ACAnalysis, self).__init__(atype)

        self.__vtype = ''
        self.__points = 0
        self.__fstart = 0
        self.__fstop = 0
    
    def set_arg(self, vtype, points, fstart, fstop):
        self.set_vtype(vtype)
        self.__points = int(points)
        self.__fstart = fstart
        self.__fstop = fstop
    
    def set_vtype(self, vtype):
        if vtype != "dec" and vtype != "oct" and vtype != "lin":
            self.__vtype = "dec"
        else:
            self.__vtype = vtype
    
    def do_analysis(self):
        pass