# -*- coding: utf-8 -*-

# Filename : isrc_model.py
# Author   : Hao Limin
# Date     : 2020-03-15
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Current Source model, inherit ModelBase.
"""

from device.base import ModelBase


class IsrcModel(ModelBase):
    def __init__(self, mtype):
        super(IsrcModel, self).__init__(mtype)
    
    def setup(self):
        pass

    def load(self):
        pass