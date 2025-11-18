import dht
import machine
import network
import time

SSID= "josue"
PASSWORD= "merchan2"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password= PASSWORD, 
authmode = network.AUTH_WPA_WPA2_PSK)
ip_address = ap.ifconfig()[0]
print(
"ESP32 configurado con access point")
print("Direccion IP del Access Point: "
, ip_address)

#ESP32 2

def do_connect(SSID, PASSWORD):
    import network
    global sta_if
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(SSID,PASSWORD)
        print('conectado a la red', SSID+"...")
        while not sta_if.isconnected():
            pass
        print('configuracion de red(IP/netmask/gw/DNS):', sta_if.ifconfig())
        
do_connect('josue','merchan2')
