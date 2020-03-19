# -*- coding: utf-8 -*-

# Filename : indmodel.py
# Author   : Hao Limin
# Date     : 2020-03-19
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Inductor model, inherit ModelBase
"""

from device.base import ModelBase


class InductorModel(ModelBase):
    def __init__(self, mtype):
        super(InductorModel, self).__init__(mtype)
    
    def setup(self, MNA, RHS):
        for l in self._device_list:
            l.setup(MNA, RHS)

    """
    Inductor(s) are shorted in dc.
    """
    def load_dc(self, MNA, RHS):
        for l in self._device_list:
            l.load_dc(MNA, RHS)

    """
    AC analysis
    """
    def load_ac(self, MNA, RHS, freq):
        for l in self._device_list:
            l.load_ac(MNA, RHS, freq)
    
    """
    Tran Analysis
    """
    def load_tran(self, MNA, RHS, time):
        pass