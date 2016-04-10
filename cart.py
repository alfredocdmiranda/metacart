#!/usr/bin/python
# -*- coding: utf-8 -*-

import struct

ADDR_ROM_TYPE = 21 #'0x15'
ROMS_TYPE = {
                32: {'name': 'LoROM', 'header': 32704},
                33: {'name': 'HiROM', 'header': 32704} , #65472
                48: 'LoROM + FastROM',
                49: 'HiROM + FastROM',
                50: 'ExLoROM',
                53: 'ExHiROM',
            }
#LOROM = 32 #'0x20'
#HIROM = 33 #'0x21'
#LOROM_FAST = 48 #'0X30'
#HIROM_FAST = 49 #'0X31'
#EXLOROM = 50 #'0X32'
#EXHIROM = 53 #'0X35'

def is_headerless(cart_data):
    len_cart_mod = len(cart_data) % 1024
    
    if len_cart_mod == 0:
        return True
    elif len_cart_mod == 512:
        return False
    else:
        raise BaseException('Invalid ROM.')

def read_cartridge(cart_data):
    """info = {}
    
    info['headerless'] = is_headerless(cart_data)
    if info['headerless']:
        offset = 0
    else:
        offset = 512
    
    type_byte = struct.unpack('B', cart_data[ADDR_ROM_TYPE])[0]
    #print(info['type'])
    info['type'] = ROMS_TYPE[type_byte]['name']
    info['name'] = struct.unpack('21s', cart_data[ROMS_TYPE[type_byte]['header']:ROMS_TYPE[type_byte]['header']+21])
    
    
    print(info)"""
    print("Name", struct.unpack('21s', cart_data[32704:32725])[0]) #Name
    print("Layout", struct.unpack('B', cart_data[32725])[0]) #Type
    print("Type",struct.unpack('B', cart_data[32726])[0]) #
    print("ROM Size (**2)", struct.unpack('B', cart_data[32727])[0])
    print("RAM Size (**2)", struct.unpack('B', cart_data[32728])[0])
    print("Country code", struct.unpack('B', cart_data[32729])[0])
    print("License code", struct.unpack('B', cart_data[32730])[0])
    print("Version", struct.unpack('B', cart_data[32731])[0])
    print("Checksum complement", struct.unpack('H', cart_data[32732:32734])[0])
    print("Checksum", struct.unpack('H', cart_data[32734:32736])[0])
    print("Unknown", struct.unpack('i', cart_data[32736:32740])[0])
    print("Vectors native", struct.unpack('6H', cart_data[32740:32752]))
    print("Unknown", struct.unpack('i', cart_data[32752:32756])[0])
    print("Vectors emulation", struct.unpack('6H', cart_data[32756:32768]))

#class Cartridge(object):
#    def __init__(self, filename):
#        pass
#
#    def read_cartridge(self, cart_data):
#        rom_type = struct.unpack('B', cart_data[ADDR_ROM_TYPE])
#
#        return

if __name__ == '__main__':
    with open('mario.sfc', 'rb') as f:
        cart_data = f.read()
    
    read_cartridge(cart_data)
