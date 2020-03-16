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

from maths.sparse.matrix import Matrix, Vector
from maths.sparse.solver import Solver


class CktInst():
    def __init__(self, write):
        self.write = write
        self.__nodes = {}           # name : Node and Branch
        self.__devices = {}         # name : Device
        self.__models = {}          # type : Model
        self.__max_number = 0

        self.__MNA = None           # Modified Nodal Matrix : A
        self.__RHS = None           # Right Hand Side : B
        self.__Solution = None      # Solution : x
        self.__solver = None        # Linear solver, solve Ax = B

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

    """
    Get device from device name.
    """
    def get_device(self, name):
        if name not in self.__devices:
            return None
        else:
            return self.__devices[name]

    """
    Print all nodes.
    """
    def print_all_nodes(self):
        for node in self.__nodes.values():
            print(node)

    """
    Print all devices.
    """
    def print_all_devices(self):
        for device in self.__devices.values():
            print(device)

    """
    Print all models.
    """
    def print_all_models(self):
        for model in self.__models.values():
            print(model)

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
            const.ISRC_TYPE     : IsrcModel,
            const.RESISTOR_TYPE : ResistorModel,
            const.VSRC_TYPE     : VsrcModel
        }

        for mtype, Model in model_dict.items():
            model = Model(mtype)
            self.__models[mtype] = model

    """
    Create all branchs, such as inductor, voltage source ...
    """
    def __create_branchs(self):
        size = len(self.__nodes)
        for d in self.__devices.values():
            if d.get_mtype() == const.INDUCTOR_TYPE:
                pass
            elif d.get_mtype() == const.VSRC_TYPE:
                branch_name = "{}#branch".format(d.get_name())
                branch = Branch(branch_name)
                branch.set_number(size)
                d.set_branch(branch)
                self.__nodes[branch_name] = branch
                size += 1

    """
    Do something after paring.
    """
    def finish_parsing(self):
        self.__create_branchs()

    """
    Setup all device.
    """
    def setup_dc(self):

        size = len(self.__nodes)

        self.__MNA = Matrix(size, 'float')
        self.__RHS = Vector(size, 'float')
        self.__solver = Solver(self.__MNA, self.__RHS)

        for model in self.__models.values():
            model.setup_dc(self.__MNA, self.__RHS)
        
        # if __debug__:
        #     print("After setup_dc operation:")
        #     self.__MNA.print_to_screen()
        #     self.__RHS.print_to_screen("Right Hand Side")
    
    def setup_ac(self):
        size = len(self.__nodes)

        self.__MNA = Matrix(size, 'complex')
        self.__RHS = Vector(size, 'complex')
        self.__solver = Solver(self.__MNA, self.__RHS)

        for model in self.__models.values():
            model.setup_ac(self.__MNA, self.__RHS)
        
        # if __debug__:
        #     print("After setup_ac operation:")
        #     self.__MNA.print_to_screen()
        #     self.__RHS.print_to_screen("Right Hand Side")

    def setup_tran(self):
        size = len(self.__nodes)

        self.__MNA = Matrix(size, 'float')
        self.__RHS = Vector(size, 'float')
        self.__solver = Solver(self.__MNA, self.__RHS)

        for model in self.__models.values():
            model.setup_tran(self.__MNA, self.__RHS)
        
        # if __debug__:
        #     print("After setup_tran operation:")
        #     self.__MNA.print_to_screen()
        #     self.__RHS.print_to_screen("Right Hand Side")
        
    """
    Load all devices.
    """
    def load_dc(self):
        for model in self.__models.values():
            model.load_dc(self.__MNA, self.__RHS)
        # if __debug__:
        #     print("After load_dc operation:")
        #     self.__MNA.print_to_screen()
        #     self.__RHS.print_to_screen("Right Hand Side")

    def load_ac(self, freq):
        for model in self.__models.values():
            model.load_ac(self.__MNA, self.__RHS, freq)
        # if __debug__:
        #     print("After load_ac operation:")
        #     self.__MNA.print_to_screen()
        #     self.__RHS.print_to_screen("Right Hand Side")

    def load_tran(self):
        for model in self.__models.values():
            model.load_tran(self.__MNA, self.__RHS)
        # if __debug__:
        #     print("After load_tran operation:")
        #     self.__MNA.print_to_screen()
        #     self.__RHS.print_to_screen("Right Hand Side")

    def solve(self):
        self.__Solution = self.__solver.solve()

    """
    Reset MNA, RHS
    """
    def reset(self):
        if self.__MNA:
            self.__MNA.clear()
        if self.__RHS:
            self.__RHS.clear()

    """
    Export simulation result
    """
    def export(self):
        self.__Solution.print_to_screen("Solution")


