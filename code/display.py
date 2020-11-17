from machine import Pin, I2C
from lib.ssd1306 import SSD1306_I2C
from lib.menu import menu as m
from lib.GFX import GFX

display_rst = Pin(16, Pin.OUT)
display_rst.value(1)

i2c = I2C(scl=Pin(15), sda=Pin(4))

oled_width = 128
oled_height = 64

display = SSD1306_I2C(oled_width, oled_height, i2c)

graphics = GFX(oled_width, oled_height, display.pixel)

menu = m(graphics, display, 0, 0, 128, 64)
