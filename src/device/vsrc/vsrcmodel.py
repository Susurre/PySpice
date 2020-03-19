# -*- coding: utf-8 -*-

# Filename : vsrcmodel.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Voltage Source model, inherit ModelBase.
"""

from device.base import ModelBase


class VsrcModel(ModelBase):
    def __init__(self, mtype):
        super(VsrcModel, self).__init__(mtype)
    
    def setup(self, MNA, RHS):
        for v in self._device_list:
            v.setup(MNA, RHS)

    """
    All Vsrc instance(s) and load_dc.
    """
    def load_dc(self, MNA, RHS):
        for v in self._device_list:
            v.load_dc(MNA, RHS)

    """
    All Vsrc instance(s) and load_ac.
    """
    def load_ac(self, MNA, RHS, freq):
        for v in self._device_list:
            v.load_ac(MNA, RHS, freq)
    
    """
    Tran Analysis
    """
    def load_tran(self, MNA, RHS, time):
        pass