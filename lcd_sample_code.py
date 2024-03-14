import time
import wiringpi
import spidev
from class_LCD import LCD, ActivateLCD, DeactivateLCD

PINS = {
    'RST' : 3,
    'CS' : 4, # CE
    'DC' : 6, # D/C
    'DIN' : 9,
    'SCLK' : 10, # CLK
    'LED' : 13, # LIGHT
}

wiringpi.wiringPiSetup()
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0) # (channel, port, speed, mode)
wiringpi.pinMode(PINS['CS'] , 1) # set pin to mode 1 (output)
ActivateLCD(PINS['CS'])
lcd_1 = LCD(PINS)

i=90
try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    
    while True:
        print (f'Counter:\n{i}')
        # LCD is activated and deactivated because of SPI
        # this enabbles other SPI components to communicate with the master
        ActivateLCD(PINS['CS'])
        lcd_1.clear() # clear buffer
        lcd_1.go_to_xy(0, 0) # starting position
        lcd_1.put_string(f'Counter:\n{i}') # print to buffer
        lcd_1.refresh() # update the LCD with the buffer
        DeactivateLCD(PINS['CS'])
        time.sleep(1)
        i += 1

except KeyboardInterrupt:
    # deactivaten the LCD after code ended
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD(PINS['CS'])
    print("\nProgram terminated")
