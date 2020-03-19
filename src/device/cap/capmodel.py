# -*- coding: utf-8 -*-

# Filename : capmodel.py
# Author   : Hao Limin
# Date     : 2020-03-14
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Capacitor model, inherit ModelBase
"""

from device.base import ModelBase


class CapacitorModel(ModelBase):
    def __init__(self, mtype):
        super(CapacitorModel, self).__init__(mtype)
    
    def setup(self, MNA, RHS):
        for c in self._device_list:
            c.setup(MNA, RHS)

    """
    Capacitor(s) are opened in dc.
    """
    def load_dc(self, MNA, RHS):
        for c in self._device_list:
            c.load_dc(MNA, RHS)

    """
    AC analysis
    """
    def load_ac(self, MNA, RHS, freq):
        for c in self._device_list:
            c.load_ac(MNA, RHS, freq)
    
    """
    Tran Analysis
    """
    def load_tran(self, MNA, RHS, time):
        pass