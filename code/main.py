from machine import Pin, I2C
import ssd1306
from time import sleep

display_rst = Pin(16, Pin.OUT)
display_rst.value(1)

i2c = I2C(scl=Pin(15), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)

oled.show()
