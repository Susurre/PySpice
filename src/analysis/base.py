# -*- coding: utf-8 -*-

# Filename : base.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Base class of other analysis.
atype : analysis type.
"""

import abc


class Analysis():
    def __init__(self, atype):
        self._atype = atype
    
    def get_atype(self):
        return self._atype
    
    def set_atype(self, atype):
        self._atype = atype
    
    @abc.abstractmethod
    def do_analysis(self, cktinst, write):
        pass

    def __str__(self):
        return "Analysis => (atype: {})".format(self._atype)
