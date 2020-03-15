# -*- coding: utf-8 -*-

# Filename : parser.py
# Author   : Hao Limin
# Date     : 2020-03-13
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Parser of PySpice.
Parse all the device(s), command(s) to build objects.
write: function.
"""

from define import status
from utils import utils

from device.devices import *
from circuit.cktinst import CktInst

import re

class Parser():
    def __init__(self, filename, cktinst, write):

        self.__filename = filename
        self.write = write

        self.__content = {}
        self.__title = ''
        self.__cktinst = cktinst

        self.status_code = status.OKAY

    def __read_file(self):
        last_line = ''
        try:
            fp = open(self.__filename, 'r')
            lines = fp.readlines()
            for lineno, line in enumerate(lines):
                line = line.strip()
                if lineno == 0:
                    self.title = line
                elif line.startswith('*'):
                    pass
                elif line == '':
                    pass
                else:
                    lineno = lineno + 1
                    line = line.lower()
                    last_line = line
                    line = line.replace("gnd", "0")
                    self.__content[lineno] = line
            
            # last line must be .ends or .end
            if not (last_line == '.ends' or last_line == '.end'):
                err_msg = "{}: Last line is illegal.".format(status.ERR_PARSE)
                self.write(err_msg, "fail")
                self.status_code = status.ERR_PARSE

        except IOError:
            err_msg = "{} : Can't open {}.".format(status.ERR_OPEN_FILE, self.__filename)
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_OPEN_FILE

        finally:
            fp.close()
    
    def parse(self):
        self.__read_file()
        if self.status_code != status.OKAY:
            self.write("{}: Parse failed ...".format(status.ERR_PARSE), 'fail')
            return status.ERR_PARSE
        last_line = ''
        for lineno, line in self.__content.items():
            if line.startswith('r'):
                self.__parse_R(line, lineno)
            elif line.startswith('c'):
                self.__parse_C(line, lineno)
            elif line.startswith('l'):
                pass
            elif line.startswith('v'):
                self.__parse_V(line, lineno)
            elif line.startswith('i'):
                self.__parse_I(line, lineno)
            elif line.startswith('.'):
                last_line = line
            else:
                self.write("Ignore line: {}".format(lineno), 'warn')

            if self.status_code != status.OKAY:
                return status.ERR_PARSE
            
        return status.OKAY
    
    """
    Resistor line :Rxxxxx node1 node2 value
    """
    def __parse_R(self, tokens, lineno):
        r_pat = r"^(r.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s*$"
        ret = re.match(r_pat, tokens, re.I)

        err_msg = "{}: Parse resistor failed in line {} ...".format(status.ERR_PARSE, lineno)
        if not ret:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return
        
        ret_tuple = ret.groups()
        if len(ret_tuple) != 4:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return
        
        error, value = utils.parse_value(ret_tuple[3])
        if error != status.OKAY:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return
        
        name = ret_tuple[0]
        n1 = self.__cktinst.get_add_node(ret_tuple[1])
        n2 = self.__cktinst.get_add_node(ret_tuple[2])

        res = Resistor(name, n1, n2, value)
        self.status_code = self.__cktinst.add_device(res)
        
    """
    Capacitor line : Cxxxxx node1 node2 value
    """
    def __parse_C(self, tokens, lineno):
        c_pat = r"^(c.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s*$"
        ret = re.match(c_pat, tokens, re.I)

        err_msg = "{}: Parse capacitor failed in line {} ..."\
                  .format(status.ERR_PARSE, lineno)
        if not ret:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return
        
        ret_tuple = ret.groups()
        if len(ret_tuple) != 4:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return

        error, value = utils.parse_value(ret_tuple[3])
        if error != status.OKAY:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return
        
        name = ret_tuple[0]
        n1 = self.__cktinst.get_add_node(ret_tuple[1])
        n2 = self.__cktinst.get_add_node(ret_tuple[2])

        cap = Capacitor(name, n1, n2, value)

        self.status_code = self.__cktinst.add_device(cap)
    
    """
    Voltage source : Vxxxxx node1 node2 <<DC> value> <<AC> value> <<TRAN> func>
    """
    def __parse_V(self, tokens, lineno):
        v_pat = r"^(v.*?)\s+(.*?)\s+(.*?)\s+(dc\s+)?(.*?\s+)?(ac\s+)?(.*?\s+)?(tran\s+)?(.*?)?\s*$"
        ret = re.match(v_pat, tokens, re.I)

        err_msg = "{}: Parse voltage source failed in line {} ..."\
                  .format(status.ERR_PARSE, lineno)
        
        if not ret:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return
        
        # if not matched, the value is None. filter None
        ret_tuple = ret.groups()
        fltr = list(filter(utils.filter_None, ret_tuple))

        if len(fltr) < 4:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return
        
        name = fltr[0]
        n1 = self.__cktinst.get_add_node(fltr[1])
        n2 = self.__cktinst.get_add_node(fltr[2])

        dc_value = None
        ac_value = None
        tran_func = None
        pre_token = ''

        for i in range(3, len(fltr)):
            token = fltr[i].strip()
            if token == 'dc':
                pre_token = 'dc'
            elif token == 'ac':
                pre_token = 'ac'
            elif token == 'tran':
                pre_token = 'tran'
            else:
                if pre_token == '':
                    if dc_value == None:
                        self.status_code, dc_value = utils.parse_value(token)
                    elif ac_value == None:
                        self.status_code, ac_value = utils.parse_value(token)
                    elif tran_func == None:
                        self.status_code, tran_func = utils.parse_tran_func(token)

                elif pre_token == 'dc':
                    self.status_code, dc_value = utils.parse_value(token)
                elif pre_token == 'ac':
                    self.status_code, ac_value = utils.parse_value(token)
                elif pre_token == 'tran':
                    self.status_code, tran_func = utils.parse_value(token)
                
                pre_token = ''
            
            if self.status_code != status.OKAY:
                self.write(err_msg, 'fail')
                self.status_code = status.ERR_PARSE
                return
            
        vsrc = Vsrc(name, n1, n2)
        vsrc.set_dc_value(dc_value)
        vsrc.set_ac_value(ac_value)
        vsrc.set_tran_func(tran_func)
        self.status_code = self.__cktinst.add_device(vsrc)

    """
    Current source : Ixxxxx node1 node2 <<DC> value> <<AC> value> <<TRAN> func>
    """
    def __parse_I(self, tokens, lineno):
        i_pat = r"^(i.*?)\s+(.*?)\s+(.*?)\s+(dc\s+)?(.*?\s+)?(ac\s+)?(.*?\s+)?(tran\s+)?(.*?)?\s*$"
        ret = re.match(i_pat, tokens, re.I)

        err_msg = "{}: Parse current source failed in line {} ..."\
                  .format(status.ERR_PARSE, lineno)
        
        if not ret:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return
        
        # if not matched, the value is None. filter None
        ret_tuple = ret.groups()
        fltr = list(filter(utils.filter_None, ret_tuple))

        if len(fltr) < 4:
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_PARSE
            return
        
        name = fltr[0]
        n1 = self.__cktinst.get_add_node(fltr[1])
        n2 = self.__cktinst.get_add_node(fltr[2])

        dc_value = None
        ac_value = None
        tran_func = None
        pre_token = ''

        for i in range(3, len(fltr)):
            token = fltr[i].strip()
            if token == 'dc':
                pre_token = 'dc'
            elif token == 'ac':
                pre_token = 'ac'
            elif token == 'tran':
                pre_token = 'tran'
            else:
                if pre_token == '':
                    if dc_value == None:
                        self.status_code, dc_value = utils.parse_value(token)
                    elif ac_value == None:
                        self.status_code, ac_value = utils.parse_value(token)
                    elif tran_func == None:
                        self.status_code, tran_func = utils.parse_tran_func(token)

                elif pre_token == 'dc':
                    self.status_code, dc_value = utils.parse_value(token)
                elif pre_token == 'ac':
                    self.status_code, ac_value = utils.parse_value(token)
                elif pre_token == 'tran':
                    self.status_code, tran_func = utils.parse_value(token)
                
                pre_token = ''
            
            if self.status_code != status.OKAY:
                self.write(err_msg, 'fail')
                self.status_code = status.ERR_PARSE
                return
            
        isrc = Isrc(name, n1, n2)
        isrc.set_dc_value(dc_value)
        isrc.set_ac_value(ac_value)
        isrc.set_tran_func(tran_func)

        self.status_code = self.__cktinst.add_device(isrc)
