from time import sleep
import api
from display import display

display.text('Main...', 0, 0)

display.show()

display.text('Getting health...', 0, 10)

health = api.get_health()

display.text(health, 0, 20)

display.show()
