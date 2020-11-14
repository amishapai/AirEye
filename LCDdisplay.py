import pyupm_i2clcd as lcd
import time
#from nanpy import Lcd

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
MAXLEN=32

def myLcd_ON ():
   myLcd.backlightOn()

# TODO Deprecate
def myLcd_DISPLAY(myStr):
   myLcd.clear()
   myLcd.setCursor(0,0)
   myLcd.write(str(myStr))

def myLcd_SETCOLOR(colorList):
   myLcd.setColor(colorList[0],colorList[1],colorList[2])

def myLcd_OFF():
   myLcd.backlightOff()

def myLcd_SCROLL(myStr):
   myLcd.clear()
   if len(myStr) > MAXLEN:
     padding = " " * MAXLEN
     oldText = myStr
     myStr = padding + myStr + " "
     for i in range (0, len(myStr)):
        #myLcd.printString(myStr[i:(i+16)], 0, 1)
        myLcd.setCursor(0,0)
        myLcd.write(myStr[i:(i+MAXLEN)])
        myLcd.setCursor(1,0)
        myLcd.write(myStr[i:(i+MAXLEN)])
        time.sleep(0.35)
        #myLcd.printString(oldText[:16], 0, 1)
        myLcd.write(oldText[:MAXLEN])
        myLcd.write(oldText[:MAXLEN])
   else:
     #myLcd.printString(myStr, 0, 1)
     myStr1 = myStr[:16]
     myStr2 = myStr[16:]
     myLcd.setCursor(0,0)
     myLcd.write(myStr1) 
     myLcd.setCursor(1,0)
     myLcd.write(myStr2)
