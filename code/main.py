from time import sleep
from machine import Pin

import api
from display import display, graphics, menu
import wifi

def show_health(health):
    display.fill(0)

    if health.is_healthy():
        display.text('API healthy', 0, 20)
    else:
        display.text('API unhealthy!', 0, 20)

    display.show()

def load_and_show_drinks_menu():
    drinks = api.get_drinks()

    show_drinks_menu(drinks)

def show_drinks_menu(items):
    display.fill(0)

    text = []

    for item in items:
        text.append([item.name, 'scrobble_item(' + str(item.id) + ')'])

    menu.initText(text)

    display.show()

def scrobble_item(item_id):
    display.fill(0)

    display.text('Scrobbling...', 0, 20)

    display.show()

    scrobble = api.post_scrobble(item_id)

    if scrobble == None:
        display.text('Something went wrong', 0, 30)
        display.show()
    else:
        display.text('Done!', 0, 30)
        display.show()

    sleep(3)

    load_and_show_drinks_menu()

def button_up_callback(pin):
    print('up')
    print(pin.value())

    display.fill(0)
    display.text('Up', 0, 0)
    display.show()

    # menu.moveUp()
    # display.show()

def button_down_callback(pin):
    print('down')
    print(pin.value())

    display.fill(0)
    display.text('Down', 0, 0)
    display.show()

    # menu.moveDown()
    # display.show()

def button_select_callback(pin):
    print('click')
    print(pin.value())

    display.fill(0)
    display.text('Click', 0, 0)
    display.show()

    # menu.click()

def setup_buttons():
    global button_up
    global button_down
    global button_select

    button_up = Pin(23, Pin.IN, Pin.PULL_UP)
    button_down = Pin(19, Pin.IN, Pin.PULL_UP)
    button_select = Pin(22, Pin.IN, Pin.PULL_UP)

    button_up.irq(trigger = Pin.IRQ_FALLING, handler = button_up_callback)
    button_down.irq(trigger = Pin.IRQ_FALLING, handler = button_down_callback)
    button_select.irq(trigger = Pin.IRQ_FALLING, handler = button_select_callback)

def main():
    # wifi.do_connect()

    display.fill(0)
    display.text('Main', 0, 0)
    display.show()

    setup_buttons()

    # health = api.get_health()
    # show_health(health)

    # if health.is_healthy():
    #     load_and_show_drinks_menu()

main()
