###AMISHA AUTHOR
###23rd Feb 2017
###Working code

import datetime
import logging

myVariables=''
myLogDirectory = ''
myFilename = ''
myFilemode = ''
myConfigFile = "Config_File-2.txt"



########################################################################################################

def getMyConfigLines (myConfigFile):    
    with open(myConfigFile) as myfile:
        configFileLines = myfile.readlines()
        return configFileLines
    
########################################################################################################
    
def getLineNum(configFileLines):
    a=0
    flag="true"
    #print("testing***",configFileLines)
    while flag=="true":
        configFileLines[a] = configFileLines[a].strip('\n')
        if configFileLines[a]=='<Store>':
            intStartLine = a
            flag="false"
        a=a+1

    flag="true"
    while flag=="true":
        print("AirEye *****",a)
        configFileLines[a] = configFileLines[a].strip('\n')
        if configFileLines[a]=='</Store>':
            intEndLine = a
            flag="false"
        a=a+1
    return(intStartLine,intEndLine)

########################################################################################################

def getMyVariables(myConfigFile,intStartLine,intEndLine) :
    with open(myConfigFile) as myfile:
        configFileLines = myfile.readlines() [intStartLine:intEndLine]

    a=0

    while a < (intEndLine):
        configFileLines[a] = configFileLines[a].strip('\n')
        myModule = configFileLines[a].split('|')
        if myModule[0] == "LogDirectory":
            myLogDirectory = myModule[1]
        if myModule[0] == "Filename":
            myFilename = myModule[1]
        if myModule[0] == "Filemode":
            myFilemode = myModule[1]
        a=a+1
    return(myLogDirectory,myFilename,myFilemode)

########################################################################################################    

def writeToFile(timestamp,sensorReading):
        #configFileLines = getMyConfigLines (myConfigFile)
        #intStartLine,intEndLine = getLineNum(configFileLines)
        #myLogDirectory,myFilename,myFilemode = getMyVariables(myConfigFile,intStartLine,intEndLine)
        myFilename="AirEyeReadings.txt"
        myFilemode="a"
        file = open(myFilename, myFilemode)    
        file.write(timestamp + ' ' + sensorReading + '\n')
        print(myFilename + ' created, check in folder')
        file.close()
########################################################################################################
def writeSensorValues(sensorReadings):
        
    #for sensorvalue in sensorReadings:
        timestm= str(datetime.datetime.now())
        writeToFile (timestm,str(sensorReadings[0]))
        

    

        

 #writeToFile("timestamp sent","505")