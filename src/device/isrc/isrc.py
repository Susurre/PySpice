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
    def __init__(self, name, n1, n2):
        super(Isrc, self).__init__(name)

        self._mtype = const.ISRC_TYPE
        self.__n1 = n1
        self.__n2 = n2

        self.__dc_value = 0
        self.__ac_value = 0
        self.__tran_func = None

    def set_dc_value(self, dc_value):
        self.__dc_value = dc_value
    
    def set_ac_value(self, ac_value):
        self.__ac_value = ac_value
    
    def set_tran_func(self, tran_func):
        self.__tran_func = tran_func
    
    def setup(self, MNA, RHS):
        pass

    def load(self):
        pass