import time
import wiringpi
import spidev
from class_LCD import LCD, ActivateLCD, DeactivateLCD

PINS = {
    'RST' : 10,
    'CS' : 13, # CE
    'DC' : 9, # D/C
    'DIN' : 11,
    'SCLK' : 14, # CLK
    'LED' : 6, # LIGHT
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
        ActivateLCD(PINS['CS'])
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string(f'Counter:\n{i}')
        lcd_1.refresh()
        DeactivateLCD(PINS['CS'])
        time.sleep(1)
        i += 1

except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD(PINS['CS'])
    print("\nProgram terminated")
