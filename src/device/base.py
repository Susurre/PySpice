# -*- coding: utf-8 -*-

# Filename : base.py
# Author   : Hao Limin
# Date     : 2020-03-13
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
This file defines Node, Branch and DeviceBase.
DeviceBase will be inherited by other devices.
"""

import abc


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
    
    def __str__(self):
        return "Node => (name: {}), (number: {})".format(self.__name, self.__number)


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
    
    def __str__(self):
        return "Branch => (name: {}), (number: {})".format(self.__name, self.__number)


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
    
    @abc.abstractmethod
    def setup(self, MNA, RHS):
        pass

    @abc.abstractmethod
    def load(self):
        pass

    def __str__(self):
        return "Device => (name: {}), (mtype: {})".format(self._name, self._mtype)

    

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
    
    @abc.abstractmethod
    def setup(self):
        pass

    @abc.abstractmethod
    def load(self):
        pass

    def __str__(self):
        dump_str = "====================\n"
        dump_str += "Model => (mtype: {})\n".format(self._mtype)
        for device in self._device_list:
            dump_str += (str(device) + "\n")
        dump_str += "===================="
        return dump_str