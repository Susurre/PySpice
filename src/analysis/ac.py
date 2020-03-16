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

from define import status


class ACAnalysis(Analysis):
    def __init__(self, atype):
        super(ACAnalysis, self).__init__(atype)

        self.__vtype = ''
        self.__points = 0
        self.__fstart = 0
        self.__fstop = 0

        self.write = None

    def set_arg(self, vtype, points, fstart, fstop):
        self.set_vtype(vtype)
        self.__points = int(points)
        self.__fstart = fstart
        self.__fstop = fstop

        if self.__vtype == "oct":
            self.__base = 2
        # dec
        else:          
            self.__base = 10
    
    def set_vtype(self, vtype):
        if vtype != "dec" and vtype != "oct" and vtype != "lin":
            self.__vtype = "dec"
        else:
            self.__vtype = vtype
    
    def get_freq_at_step(self, step):
        if self.__vtype == "lin":
            freq = (self.__fstop - self.__fstart) / (self.__points - 1) * step
        else:
            freq = self.__fstart * self.__base ** (step * 1.0 / self.__points)
        return freq

    def do_analysis(self, cktinst, write):
        
        cktinst.setup_ac()

        step = 0
        while True:
            curr_f = self.get_freq_at_step(step)
            if curr_f > self.__fstop:
                break
            cktinst.load_ac(curr_f)
            cktinst.solve()
            cktinst.export()
            cktinst.reset()

            step += 1
        
        return status.OKAY

    def __str__(self):
        line = "AC Analysis => (vtype: {}), (points: {}), (fstart: {}), (fstop: {})"\
               .format(self.__vtype, self.__points, self.__fstart, self.__fstop)
        return line