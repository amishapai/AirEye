# Get global variable

global aeSensors_connected

# Import modules

import Start as aeStart
import LCD_RGB_display
import Show as aeShow
import storeReadings as aeStore
import sense_program as aeSense
import time
import logging

# Setup logging

logging.basicConfig(filename = 'aeLog.log', level = logging.DEBUG)

# Setup timer and start sensing

timer = 0

aeSense.start_sensors()
aeStart.logMe('Started sensors','2','Started all sensors.')
logging.info('2: Started sensors.')


while True:
    timer = timer + 1
    time.sleep(1)
    if timer % 900 == 0:
        x = aeSense.read_sensors()
        aeStart.logMe('Sensing','3','Started sensing.')
        logging.info('3: Started sensing.')

        aeShow.display_unit(x)
        print ("AIREYE *****", x)
        aeStart.logMe('Displaying','4','Displaying string.')
        logging.info('4: Displaying string.')

        aeStore.writeSensorValues(x)        
        aeStart.logMe('Readings stored','5','Readings stored to file')
        logging.info('5: Readings stored to file.')
            