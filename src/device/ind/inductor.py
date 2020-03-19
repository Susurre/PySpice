# -*- coding: utf-8 -*-

# Filename : inductor.py
# Author   : Hao Limin
# Date     : 2020-03-18
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Inductor instance, inherit DeviceBase.
"""

from device.base import DeviceBase
from define import const

import math


class Inductor(DeviceBase):
    def __init__(self, name, pos_node, neg_node, inductance):
        super(Inductor, self).__init__(name)

        self._mtype = const.INDUCTOR_TYPE
        self.__pos_node = pos_node
        self.__neg_node = neg_node
        self.__inductance = inductance
        self.__branch = None
    
    def setup_dc(self, MNA, RHS):
        pass

    def load_dc(self, MNA, RHS):
        pass

    def setup_ac(self, MNA, RHS):
        pass

    def load_ac(self, MNA, RHS, freq):
        pass

    def setup_tran(self, MNA, RHS):
        pass

    def load_tran(self, MNA, RHS, time):
        pass
