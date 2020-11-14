import mraa
import datetime 

#Global Variables
myModule = 'Sense'
aeConfigFileName = "Config_File-2.txt"
aeConfigFileLines = []
aeSensors_connected = []
aeSensors_reading = []
#Formats output the required format
#[['PM2.5',20,'Good','2017-01-30 4:10PM'],['CO',5,'Moderate','2017-01-01 5:10PM']]


# List_Search finds any string in a given list of strings, returns -1 if we dont find it
# Rule : find for string only if its in the beginning of the line
# Rule : Don't put any spaces in the beginning of the file.
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
        return -1 and print("Error")

# Find pollutant limits, including min, max and label
# loads all values into pollutant_limits, returns it
def func_pollutant(pollutant):
    global aeConfigFileLines
    pollutant_limits = []

    #print ("func_pollutants::pollutant", pollutant)
    
    temp_location = List_Search(pollutant)
    if temp_location == -1:
        return []

    #print ("func_pollutants::temp_location", temp_location)
    
    temp_list = aeConfigFileLines[temp_location].split("|")
    for x in range (0,18,3):
        loop_list = []
        loop_list.append(float(temp_list[x+1]))
        loop_list.append(float(temp_list[x+2]))
        loop_list.append(temp_list[x+3])
        pollutant_limits.append(loop_list)
    #print ("pollutant_limits are:",pollutant_limits)
    return pollutant_limits

# finds and returns the config lines for a given module name 
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



# Find number of sensors
# load all sensors into aeSensors_connected
def load_sensors():
    global aeConfigFileLines
    global aeSensors_connected
    
    temp_location = List_Search('Number of sensors')
    temp_list = aeConfigFileLines[temp_location].split('|')
    num_of_sensors = int(temp_list[1])

    aeSensors_connected = []
   

    for x in range(0,num_of_sensors):
        #print("x=",x)
        sens_split = aeConfigFileLines[temp_location+1+x].split("|")
        #print("sens_split1:",sens_split)
        string_to_int  = int(sens_split[1])
        del sens_split[1]
        #print ("sens_split2:",sens_split)
        sens_split .insert(1,string_to_int)
        #print ("sens_split3:",sens_split)

        aeSensors_connected.append(sens_split)
        #input()

#    print("load_sensors::Sensors_connected:", aeSensors_connected)
    return


#Uncomment the code below when Edison kit with sensors is connected

def start_sensors():
    global aeSensors_connected
    
    for x in range (0,len(aeSensors_connected)):
        sensor_pointer = mraa.Aio(aeSensors_connected[x][1])
        aeSensors_connected[x].append(sensor_pointer)
    return


def read_sensors():
    global aeSensors_connected
    global aeSensors_reading

    for x in range (0,len(aeSensors_connected)):
        sensor_value = aeSensors_connected[x][2].read()

    print sensor_value

    #hard coded test value
    #aeSensors_reading = [['PM2.5',20,'Good','2017-01-30 4:10PM'],['CO',5,'Moderate','2017-01-01 5:10PM']]

    aeSensors_reading = []
    #real value formating
    aeSensors_reading = format_sensor_output_PM2_5 (sensor_value)

    return aeSensors_reading

''' This code should be executed from supervisor
start_sensors()
read_sensors()
'''

#print(My_Module_Config(myModule))

#Improvements done:
#Tried to removed [:-1] only if line ends with \n, but improved further...
#now using read.splitlines to read the complete file

#Setting dummy sensor value for programming purpose, assume PM2.5


#Formats output the required format
#[['PM2.5',20,'Good','2017-01-30 4:10PM'],['CO',5,'Moderate','2017-01-01 5:10PM']]
def format_sensor_output_PM2_5 (sensor_value):

    grade = "not defined"
    formated_output = []
    formated_output.append("PM2.5")
    formated_output.append(sensor_value)
    
    for x in range(0,6):
        if sensor_value >= PM2_5[x][0] and sensor_value <= PM2_5[x][1]:
            grade = PM2_5[x][2]            
            break

    formated_output.append(grade)
    myTime = str(datetime.datetime.now())
    myTime = myTime.split(".",1)
    #print ("myTime=",myTime[0])
    
    formated_output.append(myTime[0])

    global aeSensors_reading
    aeSensors_reading.append(formated_output)
    
    #print ("output :",formated_output)
    print ("reading:",aeSensors_reading)

    return aeSensors_reading


load_config_file()
load_sensors()

print("Sensors_connected:", aeSensors_connected)

#Read all pollutant limits into lists
PM2_5 = func_pollutant("PM2.5")
PM10 = func_pollutant("PM10")
NO2= func_pollutant("NO2")
O3 = func_pollutant("O3")
CO = func_pollutant("CO")
SO2 = func_pollutant("SO2")
NH3 = func_pollutant("NH3")
Pb = func_pollutant("Pb")

print ("PM2.5 limits are:" ,PM2_5)
'''
print ("PM10 limits are:" ,PM10)
print ("NO2 limits are:" ,NO2)
print ("O3 limits are:" ,O3)
print ("CO limits are:" ,CO)
print ("SO2 limits are:" ,SO2)
print ("NH3 limits are:" ,NH3)
print ("Pb limits are:" ,Pb)
'''