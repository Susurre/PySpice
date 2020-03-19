# -*- coding: utf-8 -*-

# Filename : vcvsmodel.py
# Author   : Hao Limin
# Date     : 2020-03-19
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
VCVS model, inherit ModelBase
"""

from device.base import ModelBase


class VCVSModel(ModelBase):
    def __init__(self, mtype):
        super(VCVSModel, self).__init__(mtype)
    
    def setup(self, MNA, RHS):
        for e in self._device_list:
            e.setup(MNA, RHS)

    """
    VCVS(s) are opened in dc.
    """
    def load_dc(self, MNA, RHS):
        for e in self._device_list:
            e.load_dc(MNA, RHS)

    """
    AC analysis
    """
    def load_ac(self, MNA, RHS, freq):
        for e in self._device_list:
            e.load_ac(MNA, RHS, freq)
    
    """
    Tran Analysis
    """
    def load_tran(self, MNA, RHS, time):
        pass