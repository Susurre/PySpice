# -*- coding: utf-8 -*-

# Filename : vcvs.py
# Author   : Hao Limin
# Date     : 2020-03-19
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
VCVS instance, inherit DeviceBase.
"""

from device.base import DeviceBase, Branch
from define import const

import math


class VCVS(DeviceBase):
    def __init__(self, name, pos_node, neg_node, pos_ctrl_node, neg_ctrl_node, value):
        super(VCVS, self).__init__(name)
        
        self._mtype = const.VCVS_TYPE
        self.__pos_node = pos_node
        self.__neg_node = neg_node
        self.__pos_ctrl_node = pos_ctrl_node
        self.__neg_ctrl_node = neg_ctrl_node
        self.__value = value
        self.__branch = None
    
    def setup(self, MNA, RHS):
        pass
    
    def load_dc(self, MNA, RHS):
        pass

    """
    VCVS ac analysis rule.
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

    def load_tran(self, MNA, RHS, time):
        pass
