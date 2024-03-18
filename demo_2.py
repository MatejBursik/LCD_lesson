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

buttonPin = 16

wiringpi.wiringPiSetup()
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0) # (channel, port, speed, mode)
wiringpi.pinMode(buttonPin, 0) # set pin to mode 0 (input)
wiringpi.pinMode(PINS['CS'] , 1) # set pin to mode 1 (output)
ActivateLCD(PINS['CS'])
lcd_1 = LCD(PINS)

pressed = False
try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    
    while True:
        # check if button is pressed
        if wiringpi.digitalRead(buttonPin) == 1:
            pressed = False
            print(pressed)
        elif wiringpi.digitalRead(buttonPin) == 0:
            pressed = True
            print(pressed)

        # LCD is activated and deactivated because of SPI
        # this enabbles other SPI components to communicate with the master
        ActivateLCD(PINS['CS'])
        lcd_1.clear() # clear buffer
        lcd_1.go_to_xy(0, 0) # starting position
        lcd_1.put_string(f'Pressed:\n{pressed}') # print to buffer
        lcd_1.refresh() # update the LCD with the buffer
        DeactivateLCD(PINS['CS'])

        time.sleep(0.1) # anti bouncing

except KeyboardInterrupt:
    # deactivaten the LCD after code ended
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD(PINS['CS'])
    print("\nProgram terminated")
