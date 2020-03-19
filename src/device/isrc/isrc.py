# -*- coding: utf-8 -*-

# Filename : isrc.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Current Source instance, inherit DeviceBase.
"""

from device.base import DeviceBase
from define import const


class Isrc(DeviceBase):
    def __init__(self, name, pos_node, neg_node):
        super(Isrc, self).__init__(name)

        self._mtype = const.ISRC_TYPE
        self.__pos_node = pos_node
        self.__neg_node = neg_node

        self.__dc_value = 0
        self.__ac_value = 0
        self.__tran_func = None

    def set_dc_value(self, dc_value):
        self.__dc_value = dc_value
    
    def set_ac_value(self, ac_value):
        self.__ac_value = ac_value
    
    def set_tran_func(self, tran_func):
        self.__tran_func = tran_func
    
    """
    Do not need to do anything.
    """
    def setup_dc(self, MNA, RHS):
        pass
    
    """
    Isrc DC stamp rule.
    RHS:
    N+  -dc_value
    N-  +dc_value
    """
    def load_dc(self, MNA, RHS):
        
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        dc  = self.__dc_value

        RHS.add_value(pos, -dc)
        RHS.add_value(neg,  dc)
    
    def setup_ac(self, MNA, RHS):
        pass

    """
    Isrc AC analysis stamp rule.
    RHS:
    N+  -ac_value
    N-  +ac_value
    """
    def load_ac(self, MNA, RHS, freq):
        
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        ac  = self.__ac_value             # mag

        RHS.add_value(pos, -ac)
        RHS.add_value(neg,  ac)

    def setup_tran(self, MNA, RHS):
        pass

    def load_tran(self, MNA, RHS, time):
        pass