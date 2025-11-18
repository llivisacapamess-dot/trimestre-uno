import dht
import machine
import network
import time

# Nombre de la red y contraseña para el Access Point
SSID = "josue"
PASSWORD = "merchan2"

# Configuración del punto de acceso
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password=PASSWORD,
 authmode = network.AUTH_WPA_WPA2_PSK)

ip_address = ap.ifconfig()[0]
print("ESP32 configurado como Access Point")
print("Dirección IP del Access Point:", ip_address)

# Señal del sensor en el pin 4
dht_sensor = dht.DHT11(machine.Pin(14))

while True:
    try:
        # Lectura de temperatura y humedad
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        print("Temperatura: {}°C, Humedad: {}%".format(temperature, humidity))

        time.sleep(1)
        
    except OSError as e:
        print("Error al leer el sensor:", e)
        continue

#ESP 2

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
