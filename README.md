# Drinks Drunk Arduino

## Getting started

### MakerHawk ESP32

I'm using the [MakerHawk ESP32](https://www.amazon.co.uk/MakerHawk-Development-0-96inch-Display-Compatible/dp/B076P8GRWV) board.

1. Install the Arduino IDE
1. Follow the install guide for [Heltec ESP32+LoRa Series Quick Start](https://heltec-automation-docs.readthedocs.io/en/latest/esp32/quick_start.html)

Resource:https://github.com/Heltec-Aaron-Lee/WiFi_Kit_series

### Sort of generic guide

This guide is more general.

1. Install the Arduino IDE
1. Follow the install guide for [Arduio core for the ESP32](https://github.com/espressif/arduino-esp32)
1. Select board `ESP32 Dev Module` in Arduino IDE
1. Upload!

Resource: [https://www.youtube.com/watch?v=xPlN_Tk3VLQ](https://www.youtube.com/watch?v=xPlN_Tk3VLQ)

## Connecting to wifi

1. Create a file called `env.h`
1. Insert contents:
  ```
#define wifi_ssid "your ssid"
#define wifi_password "your password"
  ```
