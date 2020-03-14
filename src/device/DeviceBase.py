# -*- coding: utf-8 -*-

# Filename : devicebase.py
# Author   : Hao Limin
# Date     : 2020-03-13
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
This file defines Node, Branch and DeviceBase.
DeviceBase will be inherited by other devices.
"""


class Node():
    def __init__(self, name):
        self.__name = name
        self.__number = 0
    
    def set_name(self, name):
        self.__name = name
    
    # number must be greater than or equal to 0.
    def set_number(self, number):
        self.__number = number
    
    def get_number(self):
        return self.__number
    
    def get_name(self):
        return self.__name


class Branch():
    def __init__(self, name):
        self.__name = name
        self.__number = 0
    
    def set_name(self, name):
        self.__name = name

    # number must be greater than or equal to 0.
    def set_number(self, number):
        self.__number = number
    
    def get_number(self):
        return self.__number
    
    def get_name(self):
        return self.__name


"""
mtype : model type
"""
class DeviceBase():
    def __init__(self, name):
        self._name = name
        self._mtype = None
    
    def get_name(self):
        return self._name
    
    def get_mtype(self):
        return self._mtype
    
    def setup(self):
        pass

    def load(self):
        pass


"""
mtype : model type
"""
class ModelBase():
    def __init__(self, mtype):
        self._mtype = mtype
        self._device_list = []
    
    def get_mtype(self):
        return self._mtype
    
    def add_device(self, device):
        self._device_list.append(device)
    
    def setup(self):
        pass

    def load(self):
        pass