# LCD_lesson

description:
describe the topic
We are using Orange 3 LTS, LCD Nokia 5110 and Jumper wires.
lcd uses SPI (what, why, how)
code explanation
wiring explanation

## Hardware

- [Orange 3 LTS](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/orange-pi-3-LTS.html)
- [LCD Nokia 5110](https://components101.com/displays/nokia-5110-lcd)
- [Jumper Wires](https://en.wikipedia.org/wiki/Jump_wire)

## Dependencies

These libraries do not come with python out of the box
- wiringpi (`pip install wiringpi`)
- spidev (`pip install spidev`)

## Orange Pi pins

Pin layout corelation between Orange Pi pins (Hardware) labeled with H and their functionality in Python code (wiringpi) labeled with W.

| H | W |   | W | H |
|---|---|---|---|---|
| 1 | 3v3 |   | 5v | 2 |
| 3 | w0 |   | 5v | 4 |
| 5 | w1 |   | GND | 6 |
| 7 | w2 |   | w3 | 8 |
| 9 | GND |   | w4 | 10 |
| 11 | w5 |   | w6 | 12 |
| 13 | w7 |   | GND | 14 |
| 15 | w8 |   | w9 | 16 |
| 17 | 3v3 |   | w10 | 18 |
| 19 | w11 |   | GND | 20 |
| 21 | w12 |   | w13 | 22 |
| 23 | w14 |   | w15 | 24 |
| 25 | GND |   | w16 | 26 |

## LCD Nokia 5110 pins

| Number | Lable | Function |
|---|---|---|
| 1 | RST | Reset |
| 2 | CE | Chip Enable |
| 3 | D/C | Data/Command Selection |
| 4 | DIN | Serial Input |
| 5 | CLK | Clock Input |
| 6 | VCC | 3.3V |
| 7 | LIGHT | Backlight Control |
| 8 | GND | Ground |

## Common problems

Check your wiring.
Are the wires connected to the correct pins.
Are the wires plugged in properly.

Check the brightness of the LCD.
You might need it to be brighter.
