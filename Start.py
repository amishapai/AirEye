# Start.py - Reads the configuration file and reads the AirEye configurations

# Import modules

import sys
import os
import datetime
import logging

# Define global variables

global error_file_exists
global module_config
global aireye_config
#global all_lines

log_file_exists = 0
error_file_exists = 0

# Define functions

def List_Search(func_List, func_String):
    func_Result = 0
    for func_Result in range(0,len(func_List)):
        location = func_List[func_Result].find(func_String)
        if location > -1:
            break
    if location == 0 :
        return func_Result
    else:
                return -1

def logMe(log_name, log_no, log_msg):
    global log_file_exists
    if log_file_exists == 0:
        if os.path.exists('log.txt') == False:
            log_file_exists = 1
            file = open('log.txt', 'a+')
            file.close()

    file = open('log.txt', 'a+')
    file.write(str(datetime.datetime.now()) + ":" + log_name + ":" + log_no + ":" + log_msg + "\n")
    #file.write(datetime.datetime.now() + ":" + log_name + ":" + log_no + ":" + log_msg)
    file.close()

def writeError(error_name, error_no, error_msg):
    global error_file_exists
    error_file_name = 'error.txt'
    if error_file_exists == 0:
        if os.path.exists(error_file_name) == False:
            error_file_exists = 1
            file = open(error_file_name, 'a+')
            file.close()

    file = open(error_file_name, 'a+')
    file.write(str(datetime.datetime.now()) + ":" + error_name + ":" + error_no + ":" + error_msg + "\n")
    file.close()

def configCheck():
    if os.path.exists('Config_File-2.txt') == False:
        print ("0: Error booting. Please try again or call a helpline.")
        log_me('Config Error','0','Config File does not exist')
        writeError('Config Error','0', 'Config File does not exist.')
    else:
        logMe('Config Exists','1','Configuration file exists.')

def readAirEye():
    file = open('Config_File-2.txt','r')
    all_lines = file.readlines()
    start = List_Search(all_lines, '<AirEye>')
    end = List_Search(all_lines, '</AirEye>')
    start = start + 1
    end = end - 1
    aireye = all_lines[start:end]
    device_name = aireye[0]
    device_number = aireye[1]
    file.close()
    print (device_name)
    print (device_number)

# Run functions

readAirEye()
configCheck()