# -*- coding: utf-8 -*-

# Filename : isrcmodel.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Current Source model, inherit ModelBase.
"""

from device.base import ModelBase


class IsrcModel(ModelBase):
    def __init__(self, mtype):
        super(IsrcModel, self).__init__(mtype)
    
    def setup(self, MNA, RHS):
        for i in self._device_list:
            i.setup(MNA, RHS)

    """
    All Isrc(s) load_dc.
    """
    def load_dc(self, MNA, RHS):
        for i in self._device_list:
            i.load_dc(MNA, RHS)

    """
    All Isrc(s) and load_ac.
    """
    def load_ac(self, MNA, RHS, freq):
        for i in self._device_list:
            i.load_ac(MNA, RHS)
    
    """
    Tran Analysis
    """
    def load_tran(self, MNA, RHS, time):
        pass