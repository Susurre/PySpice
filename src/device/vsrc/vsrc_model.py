# -*- coding: utf-8 -*-

# Filename : vsrc_model.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Voltage Source model, inherit ModelBase.
"""

from device.devicebase import ModelBase


class VsrcModel(ModelBase):
    def __init__(self, mtype):
        super(VsrcModel, self).__init__(mtype)
    
    def setup(self):
        pass

    def load(self):
        pass