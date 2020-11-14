#import pyupm_i2clcd as lcd
import time

aeConfigFileName = "Config_File-2.txt"

def My_Module_Config(func_ModuleName):
    global aeConfigFileLines

    Start_module = '<' + func_ModuleName + '>'
    End_module = '</' + func_ModuleName + '>'
    Start_Line = List_Search(Start_module)
    End_Line = List_Search(End_module)
    
    #print(Start_Line)
    #print(End_Line)
    
    return aeConfigFileLines[Start_Line+1:End_Line]


#Read the config file into

def load_config_file():
    global aeConfigFileName
    global aeConfigFileLines
    
    myFile = open(aeConfigFileName,'r')
    aeConfigFileLines = []
    aeConfigFileLines = myFile.read().splitlines()
    myFile.close()

    #print (type(aeConfigFileLines))
    #print (aeConfigFileLines)

    return

# List_Search finds any string in a given list of strings, returns -1 if we dont find it
# Rule : find for string only if its in the beginning of the line
# Rule : Don't put any spaces in the beggining of the file.
def List_Search(func_string):
    global aeConfigFileLines
    
    func_result = 0
    for func_result in range(0,len(aeConfigFileLines)):
        location = aeConfigFileLines[func_result].find(func_string)
        if location > -1:
            break
    if location == 0 :
        return func_result
    else:
        return -1

def Get_Value(name):
    default_color_line = List_Search(name)
    print("ValueLineNumber:",default_color_line)
    nameValueString = aeConfigFileLines[int(default_color_line)]
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

# eg. Display_String('Message..','255,0,255',10)
def Display_String(string,color,duration):
    print ("Display started")
    print (string)
    print (type(string))
    print (color)
    print (type(color))
    print (duration)
    print (type(duration))
    colorList = convertColor(color)
    lcd.myLcd_SETCOLOR(colorList)
    lcd.myLcd_SCROLL(string)
    lcd.myLcd_ON ()
    time.sleep(duration)
    print ("Display ended")
    return

def display_unit(sensor_readings):
    grading_map = {'Good':'Good','Satisfactory':'Fair','Moderate':'Mild','Poor':'Poor',
                   'Very Poor':'Bad','Severe':'Awful','Error':'Error'}
    for x in sensor_readings:
        if x[2]=='Good':
            Display_String(x[0]+','+str(x[1])+','+grading_map[x[2]]+','+x[3],'0,255,0',5)
        elif x[2]=='Satisfactory':
            Display_String(x[0]+','+str(x[1])+','+grading_map[x[2]]+','+x[3],'135,206,235',5)
        elif x[2]=='Moderate':
            Display_String(x[0]+','+str(x[1])+','+grading_map[x[2]]+','+x[3],'0,0,255',5)
        elif x[2]=='Poor':
            Display_String(x[0]+','+str(x[1])+','+grading_map[x[2]]+','+x[3],'128,0,128',5)
        elif x[2]=='Very Poor':
            Display_String(x[0]+','+str(x[1])+','+grading_map[x[2]]+','+x[3],'255,255,0',5)
        elif x[2]=='Severe':
            Display_String(x[0]+','+str(x[1])+','+grading_map[x[2]]+','+x[3],'255,0,0',5)
        else :
            Display_String(x[0]+','+str(x[1])+','+grading_map[x[2]]+','+x[3],'255,255,255',5)


def init_show ():
    load_config_file()
    file_lines = My_Module_Config('Show')
    print("FileLines:",file_lines)
    default_color = Get_Value('Default_Color')
    print("Default_Color:",default_color)
    default_Color_List = convertColor(default_color)        

#    error_color = Get_Value('Error_Color')
#    print("Error_Color:",error_color)
#    error_Color_List = convertColor(error_color)

#    warning_color = Get_Value('Warning_Color')
#    print("Warning_Color:",warning_color)
#    warning_Color_List = convertColor(warning_color)
    
    default_string = Get_Value('Default_String')
    print("Default_String:",default_string)
    default_duration = int(Get_Value('Default_Duration'))
    print("Default_Duration:",default_duration)

    lcd.myLcd_SETCOLOR(default_Color_List)
    lcd.myLcd_SCROLL(default_string)
    lcd.myLcd_ON ()
    time.sleep(default_duration)

#    lcd.myLcd_SETCOLOR(error_Color_List)
#    lcd.myLcd_SCROLL('Test Error Message')
#    lcd.myLcd_ON ()
#    time.sleep(default_duration)

#    lcd.myLcd_SETCOLOR(warning_Color_List)
#    lcd.myLcd_SCROLL('Test Warn Message')
#    lcd.myLcd_ON ()
#    time.sleep(default_duration)
    

init_show ()
Display_String('Red Message','255,0,0',1)
Display_String('Yellow Message','255,255,0',1)
Display_String('Purple Message','128,0,128',1)
Display_String('Blue Message','0,0,255',1)
Display_String('Sky Blue Message','135,206,235',1)
Display_String('Green Message','0,255,0',1)
#sensor_readings=aeSensors_reading 
#[['PM2.5',20,'Good','2017-01-30 4:10PM'],['CO',5,'Moderate','2017-01-01 5:10PM']]
#display_unit(sensor_readings)