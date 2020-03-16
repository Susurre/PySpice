# -*- coding: utf-8 -*-

# Filename : capacitor_model.py
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
    
    """
    All capacitor instance(s) setup.
    """
    def setup(self, MNA, RHS):
        for c in self._device_list:
            c.setup(MNA, RHS)

    def load(self):
        pass