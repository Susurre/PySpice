# -*- coding: utf-8 -*-

# Filename : resistor.py
# Author   : Hao Limin
# Date     : 2020-03-14
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Resistor instance, inherit DeviceBase.
"""

from device.devicebase import DeviceBase
from define import const


class Resistor(DeviceBase):
    def __init__(self, name, n1, n2, resistance):
        super(Resistor, self).__init__(name)
        self._mtype = const.RESISTOR_TYPE

        self.__n1 = n1
        self.__n2 = n2
        self.__resistance = resistance

