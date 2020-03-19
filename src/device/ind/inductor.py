# -*- coding: utf-8 -*-

# Filename : inductor.py
# Author   : Hao Limin
# Date     : 2020-03-18
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Inductor instance, inherit DeviceBase.
"""

from device.base import DeviceBase, Branch
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
    
    def setup(self, MNA, RHS):
        branch = Branch("{}#branch".format(self._name))
        size = MNA.get_size()    # max_node_number + 1
        branch.set_number(size)
        MNA.enlarge_matrix(size + 1)
        RHS.enlarge_vector(size + 1)
        self.__branch = branch

    """
    Inductor DC Analysis stamp rule.
    MNA:
            N+      N-      Br
    N+                       1

    N-                      -1

    Br       1       -1      0
    """
    def load_dc(self, MNA, RHS):
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        br  = self.__branch.get_number()

        MNA.add_value(pos, br,   1)
        MNA.add_value(neg, br,  -1)
        MNA.add_value(br,  pos,  1)
        MNA.add_value(br,  neg, -1)

    """
    Inductor AC Analysis stamp rule.
    MNA:
            N+      N-      Br
    N+                       1

    N-                      -1

    Br       1       -1     -sl
    """
    def load_ac(self, MNA, RHS, freq):
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        br  = self.__branch.get_number()
        l   = self.__inductance
        s   = 2 * math.pi * freq

        MNA.add_value(pos, br,   1)
        MNA.add_value(neg, br,  -1)
        MNA.add_value(br,  pos,  1)
        MNA.add_value(br,  neg, -1)
        MNA.add_value(br,  br,  -s * l)
        
    def load_tran(self, MNA, RHS, time):
        pass
