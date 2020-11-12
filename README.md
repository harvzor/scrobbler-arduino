# Drinks Drunk Arduino

## Getting started

## Arduino CLI

I'm using v0.13.

1. `choco install arduino-cli -y`
1. Find config file with `arduino-cli`
1. Add:
  ```
board_manager:
  additional_urls:
    - https://resource.heltec.cn/download/package_heltec_esp32_index.json
  ```
1. `arduino-cli core install Heltec-esp32:esp32`
1. `arduino-cli compile --fqbn Heltec-esp32:esp32:wifi_kit_32 drinks-drunk-arduino`
1. `arduino-cli board list` to find the port, mine is COM3
1. `arduino-cli upload -p COM3 --fqbn Heltec-esp32:esp32:wifi_kit_32 drinks-drunk-arduino`

Resource: https://arduino.github.io/arduino-cli/latest/getting-started/

### Serial monitor

#### Docker

I tried to get it workign via Docker on Windows and WSL2 but that's not supported yet: https://docs.microsoft.com/en-us/windows/wsl/wsl2-faq#can-i-access-the-gpu-in-wsl-2-are-there-plans-to-increase-hardware-support

> As of right now WSL 2 does not include serial support, or USB device support

#### Putty

1. `choco install putty -y`
1. open putty
1. **don't go to serial section**
1. select **Serial** option in radio buttons
1. set **Serial line** and **Speed** to `115200`
1. save profile as `Wifi32`
1. run `putty -load Wifi32` from CLI to run that profile

## Arduino IDE

### MakerHawk ESP32

I'm using the [MakerHawk ESP32](https://www.amazon.co.uk/MakerHawk-Development-0-96inch-Display-Compatible/dp/B076P8GRWV) board.

1. Install the Arduino IDE
1. Follow the install guide for [Heltec ESP32+LoRa Series Quick Start](https://heltec-automation-docs.readthedocs.io/en/latest/esp32/quick_start.html)

Resource: https://github.com/Heltec-Aaron-Lee/WiFi_Kit_series

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
