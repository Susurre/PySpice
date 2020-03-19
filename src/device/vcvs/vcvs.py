# -*- coding: utf-8 -*-

# Filename : vcvs.py
# Author   : Hao Limin
# Date     : 2020-03-19
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
VCVS instance, inherit DeviceBase.
"""

from device.base import DeviceBase, Branch
from define import const

import math


class VCVS(DeviceBase):
    def __init__(self, name, pos_node, neg_node, pos_ctrl_node, neg_ctrl_node, value):
        super(VCVS, self).__init__(name)
        
        self._mtype = const.VCVS_TYPE
        self.__pos_node = pos_node
        self.__neg_node = neg_node
        self.__pos_ctrl_node = pos_ctrl_node
        self.__neg_ctrl_node = neg_ctrl_node
        self.__value = value
        self.__branch = None
    
    def setup(self, MNA, RHS):
        branch = Branch("{}#branch".format(self._name))
        size = MNA.get_size()    # size = max_node_number + 1
        branch.set_number(size)
        MNA.enlarge_matrix(size + 1)
        RHS.enalreg_vector(size + 1)
        self.__branch = branch
    
    """
    VCVS dc analysis stamp rule.
    MNA:
            N+      N-      NC+       NC-       Br

    N+                                          +1

    N-                                          -1

    NC+

    NC-

    Br      +1       -1      -Ek       +Ek
    """
    def load_dc(self, MNA, RHS):
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        pos_ctrl = self.__pos_ctrl_node.get_number()
        neg_ctrl = self.__neg_ctrl_node.get_number()
        br = self.__branch.get_number()
        Ek = self.__value

        MNA.add_value(pos, br, 1)
        MNA.add_value(neg, br, -1)
        MNA.add_value(br, pos, 1)
        MNA.add_value(br, neg, -1)
        MNA.add_value(br, pos_ctrl, -Ek)
        MNA.add_value(br, neg_ctrl, Ek)

    """
    VCVS ac analysis stamp rule.
    MNA:
            N+      N-      NC+       NC-       Br

    N+                                          +1

    N-                                          -1

    NC+

    NC-

    Br      +1       -1      -Ek       +Ek
    """
    def load_ac(self, MNA, RHS, freq):
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        pos_ctrl = self.__pos_ctrl_node.get_number()
        neg_ctrl = self.__neg_ctrl_node.get_number()
        br = self.__branch.get_number()
        Ek = self.__value

        MNA.add_value(pos, br, 1)
        MNA.add_value(neg, br, -1)
        MNA.add_value(br, pos, 1)
        MNA.add_value(br, neg, -1)
        MNA.add_value(br, pos_ctrl, -Ek)
        MNA.add_value(br, neg_ctrl, Ek)

    """
    VCVS tran analysis stamp rule.
    MNA:
            N+      N-      NC+       NC-       Br

    N+                                          +1

    N-                                          -1

    NC+

    NC-

    Br      +1       -1      -Ek       +Ek
    """
    def load_tran(self, MNA, RHS, time):
        pos = self.__pos_node.get_number()
        neg = self.__neg_node.get_number()
        pos_ctrl = self.__pos_ctrl_node.get_number()
        neg_ctrl = self.__neg_ctrl_node.get_number()
        br = self.__branch.get_number()
        Ek = self.__value

        MNA.add_value(pos, br, 1)
        MNA.add_value(neg, br, -1)
        MNA.add_value(br, pos, 1)
        MNA.add_value(br, neg, -1)
        MNA.add_value(br, pos_ctrl, -Ek)
        MNA.add_value(br, neg_ctrl, Ek)