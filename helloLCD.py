#!/usr/bin/python
#show "Hello World on the LCD screen""
# CByrer

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

displayText = "Hello World"

lcd.clear()
lcd.message(displayText)

