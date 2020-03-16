# -*- coding: utf-8 -*-

# Filename : resistor_model.py
# Author   : Hao Limin
# Date     : 2020-03-14
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Resistor model, inherit ModelBase.
"""

from device.base import ModelBase


class ResistorModel(ModelBase):
    def __init__(self, mtype):
        super(ResistorModel, self).__init__(mtype)
    
    """
    All resiiistor instance(s) setup.
    """
    def setup_dc(self, MNA, RHS):
        for r in self._device_list:
            r.setup_dc(MNA, RHS)
        

    def load_dc(self, MNA, RHS):
        for r in self._device_list:
            r.load_dc(MNA, RHS)