# -*- encoding: utf-8 -*-

import sys
import os
import platform as pf
from uuid import getnode as get_mac
import hashlib
 
class MachineCode:
  
  def __init__(self):
    self.mac = ""
    self.cpu_info = ""
    self.uname = ""
    self.code_str = ""
    self.encrypt_code = ""

  def set_mac(self):
    self.mac = get_mac()

  def set_cpu_info(self):
    self.cpu_info = os.popen("cat /proc/cpuinfo").read()

  def set_uname(self):
    self.uname = os.popen("uname -a").read()

  def generate(self):
    self.set_mac()
    self.set_cpu_info()
    self.set_uname()
    self.code_str = self.mac.__str__() + self.cpu_info + self.uname
    self.encrypt_code =  hashlib.sha512(repr(self.code_str).encode('utf-8')).hexdigest()    

  def __call__(self):
    self.generate()
    return self.encrypt_code

if __name__ == '__main__':
  print(MachineCode()())
