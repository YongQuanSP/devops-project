from hal import hal_adc as adc
from hal import hal_led as led
from hal import hal_buzzer as buzzer
import time

adc.init()
led.init()
buzzer.init()


def Light():
    while True:
        value = adc.get_adc_value(0)
        if value <= 700:
            print("Possible Car Theft Attempt")
            led.set_output(0, 1)
            time.sleep(1)
            buzzer.short_beep(1)
        else:
            continue

