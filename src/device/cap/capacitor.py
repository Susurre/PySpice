# -*- coding: utf-8 -*-

# Filename : capacitor.py
# Author   : Hao Limin
# Date     : 2020-03-14
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Capacitor instance, inherit DeviceBase.
"""

from device.devicebase import DeviceBase
from define import const


class Capacitor(DeviceBase):
    def __init__(self, name, n1, n2, capacitance):
        super(Capacitor, self).__init__(name)
        
        self._mtype = const.CAPACITOR_TYPE
        self.__n1 = n1
        self.__n2 = n2
        self.__capacitance = capacitance