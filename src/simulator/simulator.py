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
        self.__analysis_task = None

    def simulate(self):
        self.write("Start simulating ...", 'note')

        # 1. Parse
        ret = self.__parse()
        if ret != status.OKAY:
            return status.ERR_SIMULATE
        
        if __debug__:
            self.__cktinst.print_all_nodes()
            self.__cktinst.print_all_models()
            for ana in self.__analysis_task:
                print(ana)
        
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
        
        self.__analysis_task = parser.get_analysis_task()

        self.write("Parse successfully!", 'success')
        return status.OKAY

    def __analyze(self):
        self.write("Start analyzing", 'note')
        for ana in self.__analysis_task:
            ret = ana.do_analysis(self.__cktinst, self.write)
            
            if ret != status.OKAY:
                err_msg = "{}: Analyze failed ..."
                self.write(err_msg, 'fail')
                return status.ERR_ANALYZE

        self.write("Analyze successfully!", 'success')
        return status.OKAY

    def __export(self):
        pass