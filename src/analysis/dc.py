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

from define import status


class DCAnalysis(Analysis):
    def __init__(self, atype):
        super(DCAnalysis, self).__init__(atype)

        self.__src1_name = ''
        self.__src1 = None
        self.__start1 = 0
        self.__stop1 = 0
        self.__incr1 = 0
        self.write = None
    
    def set_arg1(self, src1_name, start1, stop1, incr1):
        self.__src1_name = src1_name
        self.__start1 = start1
        self.__stop1 = stop1
        self.__incr1 = incr1
    
    def do_analysis(self, cktinst, write):
        self.write = write
        self.__src1 = cktinst.get_device(self.__src1_name)
        if not self.__src1:
            err_msg = "{}: Can't find {} in DC analysis."
            self.write(err_msg, 'fail')
            return status.ERR_ANALYZE
        
        cktinst.setup_dc()

        value = self.__start1
        while not value > self.__stop1:
            self.__src1.set_dc_value(value)
            cktinst.load_dc()
            cktinst.solve()
            cktinst.export()
            cktinst.reset()

            value += self.__incr1
        
        return status.OKAY

    def __str__(self):
        line = "DC Analysis => (src1: {}), (start1: {}), (stop1: {}), (incr1: {})"\
               .format(self.__src1_name, self.__start1, self.__stop1, self.__incr1)
        return line