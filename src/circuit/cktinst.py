# -*- coding: utf-8 -*-

# Filename : cktinst.py
# Author   : Hao Limin
# Date     : 2020-03-13
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Circuit Instance holds all the devices and nodes.
It will be used by analysis.
"""

from define import status
from define import const
from device.devices import *


class CktInst():
    def __init__(self, write):
        self.write = write
        self.__nodes = {}           # name : Node and Branch
        self.__devices = {}         # name : Device
        self.__models = {}          # type : Model
        self.__max_number = 0

        self.__create_models()
    
    def get_add_node(self, node_name):
        return self.__get_node(node_name)

    """
    1. If device exists, return ERR_DEVICE_REDIFINE.
    2. Add it to it's model and __devices.
    """
    def add_device(self, device):
        device_name = device.get_name()
        # 1. Check device
        if device_name in self.__devices:
            err_msg = "{}: Redefine {}".format(status.ERR_DEVICE_REDEFINE, device_name)
            self.write(err_msg, 'fail')
            return status.ERR_DEVICE_REDEFINE
        
        # 2. Add to model and __devices.
        mtype = device.get_mtype()
        if mtype not in self.__models:
            err_msg = "{}: {} model not exists.".format(status.ERR_NO_MODEL, mtype)
            self.write(err_msg, 'fail')
            return status.ERR_NO_MODEL
        
        model = self.__models[mtype]
        model.add_device(device)
        self.__devices[device_name] = device

        return status.OKAY

    def get_nodes_items(self):
        pass

    def get_devices_items(self):
        pass
    
    """
    Return node inst.
    If not exist, create it and add to __nodes.
    """
    def __get_node(self, name):
        if name in self.__nodes:
            return self.__nodes[name]
        
        # not exist
        if name == '0':        # gnd
            node = Node(name)
            node.set_number(0)
        else:
            node = Node(name)
            self.__max_number += 1
            node.set_number(self.__max_number)
        
        self.__nodes[name] = node
        return node

    """
    Create all the defined models.
    """
    def __create_models(self):

        model_dict = {
            const.CAPACITOR_TYPE: CapacitorModel,
            const.RESISTOR_TYPE : ResistorModel
        }

        for mtype, Model in model_dict.items():
            model = Model(mtype)
            self.__models[mtype] = model





        


