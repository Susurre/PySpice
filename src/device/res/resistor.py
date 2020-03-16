# -*- coding: utf-8 -*-

# Filename : resistor.py
# Author   : Hao Limin
# Date     : 2020-03-14
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Resistor instance, inherit DeviceBase.
"""

from device.base import DeviceBase
from define import const

import math


class Resistor(DeviceBase):
    def __init__(self, name, pos_node, neg_node, resistance):
        super(Resistor, self).__init__(name)
        self._mtype = const.RESISTOR_TYPE

        self.__pos_node = pos_node
        self.__neg_node = neg_node
        self.__resistance = resistance
        self.__conductance = 1
        self.update_conductance()

    def update_conductance(self):
        if math.fabs(self.__resistance) < 1e-3:
            self.__resistance = 1e-3
        
        self.__conductance = 1 / self.__resistance

    """
    Do not need to enlage the MNA and RHS.
    """
    def setup_dc(self, MNA, RHS):
        pass
    
    """
    Resistor's stamp reule.
    MNA:
            N+      N-
    N+     1/r     -1/r

    N-     -1/r     1/r
    """
    def load_dc(self, MNA, RHS):
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        cond = self.__conductance

        MNA.add_value(pos, pos, cond);
        MNA.add_value(pos, neg, -cond);
        MNA.add_value(neg, pos, -cond);
        MNA.add_value(neg, neg, cond);
    
    def setup_ac(self, MNA, RHS):
        pass

    def load_ac(self, MNA, RHS):
        pass
    
    def setup_tran(self, MNA, RHS):
        pass

    def load_tran(self, MNA, RHS):
        pass
