# -*- coding: utf-8 -*-

# Filename : resistor_model.py
# Author   : Hao Limin
# Date     : 2020-03-14
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Resistor model, inherit ModelBase.
"""

from device.base import ModelBase


class ResistorModel(ModelBase):
    def __init__(self, mtype):
        super(ResistorModel, self).__init__(mtype)
    
    def setup(self):
        pass

    def load(self):
        pass