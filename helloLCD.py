#!/usr/bin/python
#show "Hello World on the LCD screen""
# CByrer
import subprocess
import Adafruit_CharLCD as LCD
import time

lcd = LCD.Adafruit_CharLCDPlate()

Name = subprocess.check_output(['hostname']).strip()
displayText = Name

IP = subprocess.check_output(["hostname", "-I"])
refresh = True


while (True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message(displayText + "\n")
        lcd.set_backlight(1)
        lcd.message("Hello World\n")
        refresh = True
        time.sleep(1)
    else:
        if refresh:
            lcd.clear()
            lcd.set_backlight(1)
            lcd.message(displayText + "\n")
            lcd.message(IP)
            time.sleep(1)
            refresh = False


