from time import sleep
import api
from display import display

display.text('Main...', 0, 0)

display.show()

display.text('Getting health...', 0, 10)

health = api.get_health()

if health.status == 'Healthy':
    display.text('API healthy', 0, 20)
else:
    display.text('API unhealthy!', 0, 20)

display.show()
