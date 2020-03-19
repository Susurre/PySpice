# -*- coding: utf-8 -*-

# Filename : capacitor.py
# Author   : Hao Limin
# Date     : 2020-03-14
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Capacitor instance, inherit DeviceBase.
"""

from device.base import DeviceBase
from define import const

import math


class Capacitor(DeviceBase):
    def __init__(self, name, pos_node, neg_node, capacitance):
        super(Capacitor, self).__init__(name)
        
        self._mtype = const.CAPACITOR_TYPE
        self.__pos_node = pos_node
        self.__neg_node = neg_node
        self.__capacitance = capacitance
    
    def setup_dc(self, MNA, RHS):
        pass
    
    def load_dc(self, MNA, RHS):
        pass

    def setup_ac(self, MNA, RHS):
        pass

    """
    Capacitor ac analysis rule.
    MNA:
            N+      N-
    N+      sc      -sc

    N-      -sc      sc
    """
    def load_ac(self, MNA, RHS, freq):
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        s = 2 * math.pi * freq
        c = self.__capacitance

        MNA.add_value(pos, pos,  1j * s * c)
        MNA.add_value(pos, neg, -1j * s * c)
        MNA.add_value(neg, pos, -1j * s * c)
        MNA.add_value(neg, neg,  1j * s * c)


    def setup_tran(self, MNA, RHS):
        pass

    def load_tran(self, MNA, RHS, time):
        pass
