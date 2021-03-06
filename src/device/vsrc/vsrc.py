# -*- coding: utf-8 -*-

# Filename : vsrc.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Voltage Source instance, inherit DeviceBase.
"""

from device.base import DeviceBase
from define import const


class Vsrc(DeviceBase):
    def __init__(self, name, pos_node, neg_node):
        super(Vsrc, self).__init__(name)

        self._mtype = const.VSRC_TYPE
        self.__pos_node = pos_node
        self.__neg_node = neg_node

        self.__dc_value = 0
        self.__ac_value = 0
        self.__branch = None
        self.__tran_func = None
    
    def set_branch(self, branch):
        self.__branch = branch

    def set_dc_value(self, dc_value):
        self.__dc_value = dc_value
    
    def set_ac_value(self, ac_value):
        self.__ac_value = ac_value
    
    def set_tran_func(self, tran_func):
        self.__tran_func = tran_func
    
    def setup_dc(self, MNA, RHS):
        pass

    """
    MNA:
            N+      N-      Br
    N+      0       0       1

    N-      0       0      -1

    Br      1       -1      0

    RHS:
    N+  0
    N-  0
    Br  dc_value
    """
    def load_dc(self, MNA, RHS):
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        br  = self.__branch.get_number()
        dc = self.__dc_value

        MNA.add_value(pos, br,   1)
        MNA.add_value(neg, br,  -1)
        MNA.add_value(br,  pos,  1)
        MNA.add_value(br,  neg, -1)

        RHS.add_value(br, dc)


    def setup_ac(self, MNA, RHS):
        pass

    def load_ac(self, MNA, RHS):
        pass

    def setup_tran(self, MNA, RHS):
        pass

    def load_tran(self, MNA, RHS):
        pass