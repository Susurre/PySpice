# -*- coding: utf-8 -*-

# Filename : isrc_model.py
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
    
    """
    All Isrc(s) setup_dc and load_dc.
    """
    def setup_dc(self, MNA, RHS):
        for i in self._device_list:
            i.setup_dc(MNA, RHS)

    def load_dc(self, MNA, RHS):
        for i in self._device_list:
            i.load_dc(MNA, RHS)

    """
    All Isrc(s) setup_ac and load_ac.
    """
    def setup_ac(self, MNA, RHS):
        for i in self._device_list:
            i.setup_ac(MNA, RHS)

    def load_ac(self, MNA, RHS, freq):
        for i in self._device_list:
            i.load_ac(MNA, RHS)