# -*- coding: utf-8 -*-

# Filename : vsrc_model.py
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
    
    """
    All Vsrc instance(s) setup.
    """
    def setup_dc(self, MNA, RHS):
        for v in self._device_list:
            v.setup_dc(MNA, RHS)

    def load_dc(self, MNA, RHS):
        for v in self._device_list:
            v.load_dc(MNA, RHS)