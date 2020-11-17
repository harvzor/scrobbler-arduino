from time import sleep
import api
from display import display

display.text('Starting...', 0, 0)

display.show()

def show_health(health):
    display.fill(0)

    if health.is_healthy():
        display.text('API healthy', 0, 20)
    else:
        display.text('API unhealthy!', 0, 20)

    display.show()


def show_drinks():
    display.fill(0)

    display.text('Drinks:', 0, 10)

    drinks = api.get_drinks()

    for i, drink in enumerate(drinks, start=2):
        display.text('- ' + drink.name, 0, 10 * i)

    display.show()

while True:
    sleep(5)

    display.fill(0)
    display.text('Getting health...', 0, 10)
    display.show()

    health = api.get_health()
    show_health(health)

    if health.is_healthy:
        sleep(5)

        show_drinks()
