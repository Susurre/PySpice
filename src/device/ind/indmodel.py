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
    
    """
    Inductor(s) are opened in dc.
    """
    def setup_dc(self, MNA, RHS):
        for l in self._device_list:
            l.setup_dc(MNA, RHS)

    def load_dc(self, MNA, RHS):
        for l in self._device_list:
            l.load_dc(MNA, RHS)

    """
    AC analysis
    """
    def setup_ac(self, MNA, RHS):
        for l in self._device_list:
            l.setup_ac(MNA, RHS)

    def load_ac(self, MNA, RHS, freq):
        for l in self._device_list:
            l.load_ac(MNA, RHS, freq)
    
    """
    Tran Analysis
    """
    def setup_tran(self, MNA, RHS):
        pass

    def load_tran(self, MNA, RHS, time):
        pass