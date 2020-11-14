global aeSensors_connected
import Start as aeStart
import LCD_RGB_display
import Show as aeShow
import storeReadings as aeStore
import sense_program as aeSense
import time

i = 0

aeSense.start_sensors()
aeStart.log_me('Started sensors','2','Started all sensors.')

while True:
    i = i + 1
    time.sleep(1)
    if i % 5 == 0:
        x = aeSense.read_sensors()
        aeStart.log_me('Sensing','3','Started sensing.')
        print ("Running display_unit function with value: " + x)
        aeShow.display_unit(x)
        aeStart.log_me('Displaying','4','Displaying string.')
        print ("Running writeSensorValues function with value: " + x)
        aeStore.writeSensorValues(x)
        aeStart.log_me('Readings stored','5','Readings stored to file')