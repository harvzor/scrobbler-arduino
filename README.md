# Drinks Drunk Arduino

Decided to use MicroPython since whatever abomination of C++ sub or superset that Arduino normally uses is a huge pain to work with.

## Getting started

I'm using the [MakerHawk ESP32](https://www.amazon.co.uk/MakerHawk-Development-0-96inch-Display-Compatible/dp/B076P8GRWV) board.

- wiring diagram: https://raw.githubusercontent.com/Heltec-Aaron-Lee/WiFi_Kit_series/master/PinoutDiagram/WIFI%20Kit%2032.pdf

### MicroPython

1. install Python `choco install python3 -y`
1. check `python` and `pip` are in your PATH
1. install tool with `pip install esptool`
1. verify installation with `esptool.py -h` (I had to find that file and add a another PATH var to it)

#### Backup / restore

https://cyberblogspot.com/how-to-save-and-restore-esp8266-and-esp32-firmware/

Backup with:

```
esptool.py --port COM3 read_flash 0x0 0x800000 backup.bin
```

Restore with:

```
esptool.py --port COM3 write_flash 0x0 backup.bin 
```

#### Flashing MicroPython

https://micropython.org/download/esp32/

1. `esptool.py --chip esp32 --port COM3 erase_flash`
1. `esptool.py --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin`

#### Connect to REPL with `rshell`

1. `pip install rshell`
1. `rshell -p COM3`
1. `repl`
1. `print("Hello World!")`

#### Syncing code to the board

```
rshell -p COM3 rsync -m code /pyboard/
```

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

If you want to also send messages, also follow this: https://stackoverflow.com/questions/4999280/how-to-send-characters-in-putty-serial-communication-only-when-pressing-enter

## Docs

- using OLED display: https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/
- MakerHawk ESP32 wiring diagram: https://raw.githubusercontent.com/Heltec-Aaron-Lee/WiFi_Kit_series/master/PinoutDiagram/WIFI%20Kit%2032.pdf
