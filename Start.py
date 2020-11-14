import sys
import os
import datetime


global error_file_exists
global module_config
global aireye_config

log_file_exists = 0
error_file_exists = 0

# Define functions

def log_me(log_name, log_no, log_msg):
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

def write_error(error_name, error_no, error_msg):
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

def config_check():
    if os.path.exists('Config_File-2.txt') == False:
        print ("0001: Error booting. Please try again or call a helpline.")
        log_me('Config Error','0001','Config File does not exist')
        write_error('Config Error','0001', 'Config File does not exist.')

def read_AirEye():
    file = open('Config_File-2.txt','r')
    all_lines = file.readlines()
    start = List_Search(all_lines, '<AirEye>')
    end = List_Search(all_lines, '</AirEye>')
    aireye = all_lines[start:end]
    name = aireye[1]
    number = aireye[2]
    file.close()
    print (name)
    print (number)

def sense_timer():
    while 1 == 1:
        sense()
        time.sleep(900)