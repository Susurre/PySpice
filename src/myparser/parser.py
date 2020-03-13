# -*- coding: utf-8 -*-

# Filename : parser.py
# Author   : Hao Limin
# Date     : 2020-03-13
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5

"""
Parser of PySpice.
Parse all the device(s), command(s) to build objects.
"""

from define import status

class Parser():
    def __init__(self, filename, write):

        self.filename = filename
        self.write = write

        self.content = {}
        self.title = ''

        self.status_code = status.OKAY

    def read_file(self):
        try:
            fp = open(self.filename, 'r')
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
                    line = line.replace("gnd", "0")
                    self.content[lineno] = line

        except IOError:
            err_msg = "{} : Can't open {}.".format(status.ERR_OPEN_FILE, self.filename)
            self.write(err_msg, 'fail')
            self.status_code = status.ERR_OPEN_FILE

        finally:
            fp.close()

    def parse(self):
        self.read_file()

        if self.status_code != status.OKAY:
            self.write("{} : Parse failed ...".format(status.ERR_PARSE), 'fail')
            return status.ERR_PARSE
        last_line = ''
        for lineno, line in self.content.items():
            if line.startswith('r'):
                self.parse_R(line, lineno)
            elif line.startswith('c'):
                pass
            elif line.startswith('l'):
                pass
            elif line.startswith('v'):
                pass
            elif line.startswith('i'):
                pass
            elif line.startswith('.'):
                last_line = line
            else:
                self.write("Ignore line: {}".format(lineno), 'warn')

            if self.status_code != status.OKAY:
                return status.ERR_PARSE
            
        # last line must be .ends or .end
        if not (last_line == '.ends' or last_line == '.end'):
            err_msg = "{}: Last line is illegal.".format(status.ERR_PARSE)
            self.write(err_msg, "fail")
            return status.ERR_PARSE
        
        return status.OKAY
    
    """
    Resistor line :Rxxxxx node1 node2 value
    """
    def parse_R(self, tokens, lineno):
        pass

    """
    Capacitor line : Cxxxxx node1 node2 value
    """
    def parse_C(self, tokens, lineno):
        pass


