from machine import Pin
import random
from machine import Pin, SoftI2C
from I2C_LCD import I2cLcd


from time import sleep_ms
led = Pin(11, Pin.OUT)
takki = Pin(12, Pin.IN, Pin.PULL_UP)



                                                    
while True:
    if takki.value() == 0:
                # Skjárinn nota I2C tengingu til að tala við ESP
        randomtala = random.randint(1,6)
        i2c = SoftI2C(scl=Pin(13), sda=Pin(14), freq=400000)
        # print(i2c.scan()) # sýnir addressurnar á skjáunum sem eru tengdir við 13 og 14
        #lcd = I2cLcd(i2c, 0x3f, 2, 16)
        # EÐA ef þú færð villu á línuna hér fyrir ofan
        lcd = I2cLcd(i2c, 39, 2, 16)

        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr(str(randomtala))
        print(randomtala)


        if randomtala == 6:
            led.value(1)
            sleep_ms(500)
    sleep_ms(100)
    led.value(0)
