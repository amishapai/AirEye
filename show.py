#import pyupm_i2clcd as lcd
import time

def read_config_module(configFileName,moduleName):
    #myModule = 'Sense'
    myFile = open(configFileName,'r')

    myLine = myFile.readline()
    number_of_modules = int(myLine)
    #print("variable type is",type(number of modules))

    file_lines = []
    while (1):
        myLine = myFile.readline()
        if myLine == "":
            break
        file_lines.append(myLine[:-1])

    #print (file_lines)
    myMod_location = List_Search(file_lines,moduleName)
    #print("found the string in location ", myMod_location)

    if myMod_location == -1:
        print("Didn't find the module")
    else:
        Module_start_end_points = file_lines[myMod_location].split('|')
        print("Module start end points:",Module_start_end_points)
    # Rule : Don't put any spaces in the beggining of the file.

    return file_lines[int(Module_start_end_points[1])-1:int(Module_start_end_points[2])]

def List_Search(func_List,func_String):
    func_Result = 0
    for func_Result in range(0,len(func_List)):
        location = func_List[func_Result].find(func_String)
        if location > -1:
            break
    if location == 0 :
        return func_Result;
    else:
        return -1;

def Get_Value(file_lines,name):
    default_color_line = List_Search(file_lines, name)
    nameValueString = file_lines[int(default_color_line)]
    print("NameValueString:",nameValueString)
    nameValueList = nameValueString.split('|')
    return nameValueList[1]

def convertColor(colorStr):
    colorList = colorStr.split(',')
    i = 0
    for color in colorList:
        colorList[i] = int(color)
        i+=1
    return colorList
    
import LCD_RGB_display as lcd

# 
# eg. Display_String('Message..','255,0,255',10)
def Display_String(string,color,duration):
    colorList = convertColor(color)
    lcd.myLcd_SETCOLOR(colorList)
    lcd.myLcd_SCROLL(string)
    lcd.myLcd_ON ()
    time.sleep(duration)    

# TODO if color or duration use defaults from config file

def init_show ():
    file_lines = read_config_module('Config_File.txt','Show')
    print("FileLines:",file_lines)
    default_color = Get_Value(file_lines,'Default_Color')
    print("Default_Color:",default_color)
    default_Color_List = convertColor(default_color)        

    error_color = Get_Value(file_lines,'Error_Color')
    print("Error_Color:",error_color)
    error_Color_List = convertColor(error_color)

    warning_color = Get_Value(file_lines,'Warning_Color')
    print("Warning_Color:",warning_color)
    warning_Color_List = convertColor(warning_color)
    
    default_string = Get_Value(file_lines,'Default_String')
    print("Default_String:",default_string)
    default_duration = int(Get_Value(file_lines,'Default_Duration'))
    print("Default_Duration:",default_duration)

    lcd.myLcd_SETCOLOR(default_Color_List)
    lcd.myLcd_SCROLL(default_string)
    lcd.myLcd_ON ()
    time.sleep(default_duration)

    lcd.myLcd_SETCOLOR(error_Color_List)
    lcd.myLcd_SCROLL('Test Error Message')
    lcd.myLcd_ON ()
    time.sleep(default_duration)

    lcd.myLcd_SETCOLOR(warning_Color_List)
    lcd.myLcd_SCROLL('Test Warn Message')
    lcd.myLcd_ON ()
    time.sleep(default_duration)
    # TODO check if this needs to be turned off    
    #lcd.myLcd_OFF ()

init_show ()
Display_String('Test Message','255,0,255',10)