###AMISHA AUTHOR
###23rd Feb 2017
###Working code

import datetime
import logging
myVariables=''
myLogDirectory = ''
myFilename = ''
myFilemode = ''
myConfigFile = "Config_File.txt"



########################################################################################################

def getMyConfigLines (myConfigFile):    
    with open(myConfigFile) as myfile:
        configFileLines = myfile.readlines() 
        return configFileLines
    
########################################################################################################
    
def getLineNum(configFileLines):
    a=0
    flag="true"

    while flag=="true":
        configFileLines[a] = configFileLines[a].strip('\n')
        myModule = configFileLines[a].split('|')
        if configFileLines[a]=='<Store>':
            intStartLine = a
            flag="false"
        a=a+1

    flag="true"
    while flag=="true":
        configFileLines[a] = configFileLines[a].strip('\n')
        myModule = configFileLines[a].split('|')
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

    while a < (intEndLine-1):
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
        configFileLines = getMyConfigLines (myConfigFile)
        intStartLine,intEndLine = getLineNum(configFileLines)
        myLogDirectory,myFilename,myFilemode = getMyVariables(myConfigFile,intStartLine,intEndLine)

        file = open(myFilename, myFilemode ,encoding = "utf-8")    
        file.write(timestamp + ' ' + sensorReading + '\n')
        print(myFilename + ' created, check in folder')
        file.close()
########################################################################################################

'''        

writeToFile("timestamp sent","505")
'''