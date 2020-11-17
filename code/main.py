from time import sleep
import api
from display import display, graphics, menu

display.text('Starting...', 0, 0)

display.show()

def show_health(health):
    display.fill(0)

    if health.is_healthy():
        display.text('API healthy', 0, 20)
    else:
        display.text('API unhealthy!', 0, 20)

    display.show()

def show_drinks_menu(drinks):
    display.fill(0)

    text = []

    for drink in drinks:
        text.append([drink.name, 'increment_drink(' + str(drink.id) + ')'])

    menu.initText(text)

    display.show()

def increment_drink(drink_id):
    print(drink_id)

health = api.get_health()
show_health(health)

if health.is_healthy():
    sleep(5)

    drinks = api.get_drinks()

    show_drinks_menu(drinks)
