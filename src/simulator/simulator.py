# -*- coding: utf-8 -*-

# Filename : simulator.py
# Author   : Hao Limin
# Date     : 2020-03-13
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Simulator is the manager of PySpice simulation.
This class is called by GUI's simulate function.
It's will do all the analyis tasks.
"""

"""
file  : netlist filename
write : (msg, mtype) function to write log.
"""

from myparser.parser import Parser
import define.status as status

from circuit.cktinst import CktInst


class Simulator():
    def __init__(self, filename, write):
        self.__filename = filename
        self.write = write
        self.__cktinst = CktInst(self.write)

    def simulate(self):
        self.write("Start simulating ...", 'note')

        # 1. Parse
        ret = self.__parse()
        if ret != status.OKAY:
            return status.ERR_SIMULATE
        
        if __debug__:
            self.__cktinst.print_all_nodes()
            self.__cktinst.print_all_models()
        
        # 2. Analyze
        ret = self.__analyze()
        if ret != status.OKAY:
            return status.ERR_SIMULATE

        return status.OKAY
    
    def __parse(self):
        self.write("Start parsing ...", 'note')

        parser = Parser(self.__filename, self.__cktinst, self.write)
        ret = parser.parse()

        if ret != status.OKAY:
            return status.ERR_PARSE

        return status.OKAY

    def __analyze(self):
        return status.OKAY

    def __export(self):
        pass