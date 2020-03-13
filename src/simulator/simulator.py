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


class Simulator():
    def __init__(self, filename, write):
        self.filename = filename
        self.write = write

    def simulate(self):
        self.write('Start simulating ...', 'note')

        parser = Parser(self.filename, self.write)
        ret = parser.parse()

        if ret != status.OKAY:
            return status.ERR_SIMULATE

        return status.OKAY