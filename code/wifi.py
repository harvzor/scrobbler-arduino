import env
import network

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(env.wifi_ssid, env.wifi_password)
        # sta_if.connect('o2-WLAN63', '4CY2YLCB777CG83D')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
