#!/bin/bash

set -x

arduino-cli.exe compile --fqbn Heltec-esp32:esp32:wifi_kit_32 drinks-drunk-arduino
