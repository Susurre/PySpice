# -*- coding: utf-8 -*-

# Filename : utils.py
# Author   : Hao Limin
# Date     : 2020-03-13
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Utility functions.
"""

from define import status

import re


# Unit of symbols
Unit = {
    "f": 1e-15,
    "p": 1e-12,
    "n": 1e-9,
    "u": 1e-6,
    "m": 1e-3,
    "k": 1e3,
    "meg": 1e6,
    "g": 1e9,
    "t": 1e12
}


"""
Parse value from value_str : number<unit><s/hz/h>
"""
def parse_value(value_str):
    pat = r"^([+-]?[0-9]*\.?[0-9]+(?:e[+-]?[0-9]+)?)([a-z]*)?\s*$"
    ret = re.match(pat, value_str, re.I)
    
    if not ret:
         return status.ERR_PARSE, 0
    
    ret_tuple = ret.groups()
    value = eval(ret_tuple[0])
    # not None
    if ret_tuple[1]:
        unit_str = ret_tuple[1]
        unit_pat = r"^(f|p|n|u|k|meg|m|g|t)?h?z?s?$"
        unit_ret = re.match(unit_pat, unit_str, re.I)
        if not unit_ret:
            return status.ERR_PARSE, 0
        # group(1) : the first matched.
        value = value * Unit[unit_ret.group(1)]
    
    return status.OKAY, value


def parse_tran_func(func_str):
    return status.OKAY, func_str


"""
filter None in iterable
"""
def filter_None(value):
    if not value:
        return False
    else:
        return True


if __name__ == '__main__':
    value_str = "0.1khz"
    ret, value = parse_value(value_str)
    print(ret, value)
